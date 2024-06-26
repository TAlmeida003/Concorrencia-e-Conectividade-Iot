import os
import sys
import threading
import time
from Sensor import Sensor
from User import get_request
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
import View


def iniciar_conexao(sensor: Sensor) -> None:
    View.get_clear_prompt()
    print((View.get_paint_color() + "conectando ao servidor...").center(170))
    try:
        connect(sensor)
        View.get_clear_prompt()
    except RuntimeError as e:
        View.get_clear_prompt()
        View.get_report_error(e.__str__())


def connect(sensor: Sensor) -> None:
    sensor.connectBroker()
    threading.Thread(target=receive_and_respond, args=[sensor], name="Receber dados TCP").start()
    threading.Thread(target=get_option_Serve_udp, args=[sensor], name="Mandar dados UDP").start()


def receive_and_respond(sensor: Sensor) -> None:
    while True:
        try:
            msg: dict = sensor.receiveMessage()
            get_option_Serve(msg, sensor)
        except RuntimeError:
            if not sensor.auto_connect:
                threading.Thread(target=auto_connect, args=[sensor], name="Reconexão automática").start()
            if sensor.visual:
                get_request(sensor)
            break


def auto_connect(sensor: Sensor) -> None:
    while not sensor.__connected__ and not sensor.exit and sensor.user_connected:
        sensor.auto_connect = True
        try:
            connect(sensor)
        except RuntimeError:
            if sensor.visual:
                get_request(sensor)
            time.sleep(5)
    sensor.auto_connect = False


def get_option_Serve(user_choice: dict, sensor: Sensor) -> None:
    resposta: dict = {"success": True, "IP": sensor.__IP__, "descript": ""}
    try:
        sensor.set_option_serve(user_choice["option"])

        if user_choice["option"] == sensor.__server_options__[0][0]:  # ligar
            sensor.turnOn()
            resposta["descript"] = "Sensor ligado."
        elif user_choice["option"] == sensor.__server_options__[1][0]:  # desligar
            sensor.turnOff()
            resposta["descript"] = "Sensor desligado."
        elif (user_choice["option"] == sensor.__server_options__[2][0] or
              user_choice['option'] == sensor.__server_options__[3][0]):
            if sensor.visual:
                get_request(sensor)
            return
        elif user_choice["option"] == sensor.__server_options__[4][0]:  # reiniciar
            sensor.restart()
            resposta["descript"] = "Sensor reiniciado."
        elif user_choice["option"] == sensor.__server_options__[5][0]:  # nome
            sensor.setName(user_choice["value"])
            resposta["descript"] = "Nome alterado."
        elif user_choice["option"] == "data":
            resposta = sensor.get_info()
            resposta["success"] = True
        elif user_choice["option"] == "opcoes":
            resposta = {"option": sensor.get_list_options(), "success": True}
        elif user_choice["option"] == "teste":
            resposta = {"success": True, "option": "teste", "descript": "Teste de comunicação"}
    except RuntimeError as e:
        resposta = {"success": False, "code": 400, "descript": e.__str__()}

    sensor.sendMessageTCP(resposta.__str__())

    if sensor.visual:
        get_request(sensor)


def get_option_Serve_udp(sensor: Sensor) -> None:
    while sensor.__connected__:
        try:
            while sensor.is_continuous_mod():
                msg: dict = {"success": True, "IP": sensor.__IP__, "descript": ""}

                if sensor.__exe_serve_atual__ == sensor.__server_options__[2][0]:
                    msg["descript"] = f"Temperatura atual: {sensor.get_temperature()}°C."
                else:
                    msg["descript"] = f"Umidade atual: {sensor.get_humidity()}%."

                sensor.sendMessageUDP(msg.__str__())
                time.sleep(1)
        except RuntimeError as e:
            if e.__str__() == "Broker desconectado":
                break
            msg = {"success": False, "code": 400, "descript": e.__str__()}
            sensor.sendMessageUDP(msg.__str__())
