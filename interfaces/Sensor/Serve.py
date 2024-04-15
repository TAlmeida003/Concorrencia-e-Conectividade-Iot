import threading
from Sensor import Sensor
import Screen


def iniciar_conexao(sensor: Sensor) -> None:
    print("conectando ao servidor...".center(170))
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

        if user_choice == sensor.__server_options__[0]:  # ligar
            sensor.turnOn()
            resposta["descript"] = "Sensor ligado."
        elif user_choice == sensor.__server_options__[1]:  # desligar
            sensor.turnOff()
            resposta["descript"] = "Sensor desligado."
        elif (user_choice == sensor.__server_options__[2] or user_choice == sensor.__server_options__[3]) and not \
                (sensor.__exe_serve_atual__ == sensor.__server_options__[2] or
                 sensor.__exe_serve_atual__ == sensor.__server_options__[3]):
            sensor.get_temperature()
            sensor.__exe_serve_atual__ = user_choice
            return
        elif user_choice == sensor.__server_options__[2] or user_choice == sensor.__server_options__[3]:
            sensor.__exe_serve_atual__ = user_choice
            return
        elif user_choice == sensor.__server_options__[4]:  # reiniciar
            sensor.restart()
            resposta["descript"] = "Sensor reiniciado."
        elif user_choice == "data":
            resposta = sensor.get_info()
        elif user_choice == "opcoes":
            resposta = {"opcoes": sensor.get_list_options()}
        elif user_choice == "teste":
            return
    except RuntimeError as e:
        resposta = {"success": False, "code": 400, "message": e.__str__()}

    sensor.sendMessageTCP(resposta.__str__())


def mod_continuo(sensor: Sensor) -> None:
    msg: dict = {"success": True, "IP": sensor.__IP__, "descript": ""}
    while True:
        try:
            while sensor.is_continuous_mod():
                if not sensor.__state__:
                    msg = {"success": False, "code": 400, "message": "Sensor foi desligado fisicamente"}
                elif sensor.__exe_serve_atual__ == sensor.__server_options__[2]:
                    msg["descript"] = f"Temperatura atual: {sensor.__temperature__}."
                else:
                    msg["descript"] = f"Umidade atual: {sensor.__humidity__}."
                sensor.sendMessageUDP(msg.__str__())
                msg: dict = {"success": True, "IP": sensor.__IP__, "descript": ""}
        except RuntimeError as e:
            if e.__str__() == "Broker desconectado":
                break
            else:
                msg = {"success": False, "code": 400, "message": e.__str__()}
                sensor.sendMessageUDP(msg.__str__())
