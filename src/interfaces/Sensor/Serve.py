import threading
import time
from Sensor import Sensor
import Screen


def iniciar_conexao(sensor: Sensor) -> None:
    print((Screen.get_paint_color() + "conectando ao servidor...").center(170))
    try:
        sensor.connectBroker()
        threading.Thread(target=receive_and_respond, args=[sensor]).start()
        threading.Thread(target=mod_continuo, args=[sensor]).start()
        Screen.get_clear_prompt()
    except RuntimeError as e:
        Screen.get_clear_prompt()
        Screen.get_report_error(e.__str__())


def receive_and_respond(sensor: Sensor) -> None:
    while True:
        try:
            msg: dict = eval(sensor.receiveMessage())
            get_option_Serve(msg["option"], sensor)
        except RuntimeError as e:
            break


def get_option_Serve(user_choice: str, sensor: Sensor) -> None:
    resposta: dict = {"success": True, "IP": sensor.__IP__, "descript": ""}
    try:
        sensor.set_option_serve(user_choice)

        if user_choice == sensor.__server_options__[0][0]:  # ligar
            sensor.turnOn()
            resposta["descript"] = "Sensor ligado."

        elif user_choice == sensor.__server_options__[1][0]:  # desligar
            sensor.turnOff()
            resposta["descript"] = "Sensor desligado."

        elif user_choice == sensor.__server_options__[2][0] or user_choice == sensor.__server_options__[3][0]:
            return

        elif user_choice == sensor.__server_options__[4][0]:  # reiniciar
            sensor.restart()
            resposta["descript"] = "Sensor reiniciado."

        elif user_choice == "data":
            resposta = sensor.get_info()
            resposta["success"] = True

        elif user_choice == "opcoes":
            resposta = {"option": sensor.get_list_options()}
            resposta["success"] = True

        elif user_choice == "teste":
            resposta = {"success": True, "option": "teste", "descript": "Teste de comunicação"}

    except RuntimeError as e:
        resposta = {"success": False, "code": 400, "descript": e.__str__()}

    sensor.sendMessageTCP(resposta.__str__())


def mod_continuo(sensor: Sensor) -> None:
    while True:
        try:
            while sensor.is_continuous_mod():
                msg: dict = {"success": True, "IP": sensor.__IP__, "descript": ""}

                if sensor.__exe_serve_atual__ == sensor.__server_options__[2][0]:
                    msg["descript"] = f"Temperatura atual: {sensor.get_temperature()}ºC."
                else:
                    msg["descript"] = f"Umidade atual: {sensor.get_humidity()}%."
                sensor.sendMessageUDP(msg.__str__())

                time.sleep(1)
        except RuntimeError as e:
            if e.__str__() == "Broker desconectado":
                break
            else:
                msg = {"success": False, "code": 400, "descript": e.__str__()}
                sensor.sendMessageUDP(msg.__str__())
