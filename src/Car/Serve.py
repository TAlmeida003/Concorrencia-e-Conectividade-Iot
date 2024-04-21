import threading
import time

import View
from Car import Car


def iniciar_conexao(car: Car) -> None:
    print("conectando ao servidor...".center(170))
    try:
        car.connectBroker()
        threading.Thread(target=receive_and_respond, args=[car]).start()
        threading.Thread(target=get_option_Serve_udp, args=[car]).start()
        View.get_clear_prompt()
    except RuntimeError as e:
        View.get_clear_prompt()
        View.get_report_error(e.__str__())


def receive_and_respond(car: Car) -> None:
    while True:
        try:
            msg: dict = eval(car.receiveMessage())
            get_option_Serve_tcp(msg, car)
        except RuntimeError as e:
            break


def get_option_Serve_tcp(pack_msg: dict, car: Car) -> None:
    resposta: dict = {"success": True, "IP": car.ip, "descript": ""}

    try:
        car.set_option(pack_msg["option"])

        if pack_msg["option"] == "data":
            resposta = car.get_info()
            resposta["success"] = True

        elif pack_msg["option"] == "teste":
            resposta = {"success": True, "option": "teste", "descript": "Teste de comunicação"}

        elif pack_msg["option"] == "opcoes":
            resposta = {"option": car.get_list_options(), "success": True}

        elif pack_msg["option"] == car.server_option[0][0]:  # Ligar
            car.turnOn()
            resposta["descript"] = "Veículo Ligado"

        elif pack_msg["option"] == car.server_option[1][0]:  # desligar
            car.turnOff()
            resposta["descript"] = "Veículo desligado"

        elif pack_msg["option"] == car.server_option[2][0]:  # pegar velociade
            return

        elif pack_msg["option"] == car.server_option[3][0]:  # definir velocidade
            try:
                value: int = int(pack_msg["value"])
            except ValueError:
                raise RuntimeError("Campo destinado a números inteiros.")
            car.set_speed(value)
            resposta["descript"] = f"Velocidade definida para {value}Km/h"

        elif pack_msg["option"] == car.server_option[4][0]:  # travar porta
            car.lock_door()
            resposta["descript"] = "Porta travada"

        elif pack_msg["option"] == car.server_option[5][0]:  # destravar porta
            car.unlock_door()
            resposta["descript"] = "Porta destravada"

        elif pack_msg["option"] == car.server_option[6][0]:  # ir para frente
            car.go_forward()
            resposta["descript"] = "A direção do veículo está para frente"

        elif pack_msg["option"] == car.server_option[7][0]:  # ir para tras
            car.go_backward()
            resposta["descript"] = "A direção do veículo está para trás"

        elif pack_msg["option"] == car.server_option[8][0]:  # parar
            car.stop()
            resposta["descript"] = "Veículo está parado"

        elif pack_msg["option"] == car.server_option[9][0]:  # iniciar movimento
            car.start_movement()
            resposta["descript"] = "Veículo em movimento"

        elif pack_msg["option"] == car.server_option[10][0]:  # ativa buzina
            pass

        elif pack_msg["option"] == car.server_option[11][0]:  # desativar buzina
            pass

        elif pack_msg["option"] == car.server_option[12][0]:  # distancia
            return

        elif pack_msg["option"] == car.server_option[13][0]:   # status
            return

    except RuntimeError as e:
        resposta = {"success": False, "code": 400, "descript": e.__str__()}

    car.sendMessageTCP(resposta.__str__())


def get_option_Serve_udp(car: Car) -> None:
    while True:
        try:
            while car.is_continuo():
                msg: dict = {"success": True, "IP": car.ip, "descript": ""}

                if car.current_server_exe == car.server_option[2][0]:  # velocidade
                    msg["descript"] = f"Velocidade: {car.get_speed()}Km/h."
                elif car.current_server_exe == car.server_option[13][0]:  # status
                    msg = car.get_status()
                else:  # distancia
                    msg["descript"] = f"Carro se movimento {round(car.get_distance(), 1)}m do pronto de inicio."

                car.sendMessageUDP(msg.__str__())
                time.sleep(1)
        except RuntimeError as e:
            if e.__str__() == "Broker desconectado":
                break
            else:
                msg = {"success": False, "code": 400, "descript": e.__str__()}
                car.sendMessageUDP(msg.__str__())

