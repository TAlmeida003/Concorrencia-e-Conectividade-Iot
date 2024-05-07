import os
import sys
import threading
import time
from Car import Car


parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
import View


def start_connect(car: Car) -> None:
    View.get_clear_prompt()
    print((View.get_paint_color() + "conectando ao servidor...").center(170))
    try:
        connect(car)
        View.get_clear_prompt()
    except RuntimeError as e:
        View.get_clear_prompt()
        View.get_report_error(e.__str__())


def connect(car: Car) -> None:
    car.connectBroker()
    threading.Thread(target=receive_and_respond, args=[car], name="Receber dados TCP").start()
    threading.Thread(target=get_option_Serve_udp, args=[car], name="Mandar dados UDP").start()


def receive_and_respond(car: Car) -> None:
    while True:
        try:
            msg: dict = car.receiveMessage()
            get_option_Serve_tcp(msg, car)
        except RuntimeError:
            if car.visual:
                car.get_request()
            if not car.auto_connect:
                threading.Thread(target=auto_connect, args=[car], name="Reconexão automática").start()
            break


def auto_connect(car: Car) -> None:
    while not car.__connected__ and not car.exit and car.user_connected:
        car.auto_connect = True
        try:
            connect(car)
        except RuntimeError:
            if car.visual:
                car.get_request()
            time.sleep(5)
    car.auto_connect = False


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
            if car.visual:
                car.get_request()
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
            car.on_buzzer()
            resposta["descript"] = "Buzina ativada"
        elif pack_msg["option"] == car.server_option[11][0]:  # desativar buzina
            car.off_buzzer()
            resposta["descript"] = "Buzina desativada"
        elif pack_msg["option"] == car.server_option[12][0]:  # distancia
            if car.visual:
                car.get_request()
            return
        elif pack_msg["option"] == car.server_option[13][0]:  # status
            if car.visual:
                car.get_request()
            return
        elif pack_msg["option"] == car.server_option[14][0]: # gasolina
            if car.visual:
                car.get_request()
            return
        elif pack_msg["option"] == car.server_option[15][0]: # bateria
            if car.visual:
                car.get_request()
            return
        elif pack_msg["option"] == car.server_option[16][0]: #Colisao
            if car.visual:
                car.get_request()
            return
    except RuntimeError as e:
        resposta = {"success": False, "code": 400, "descript": e.__str__()}

    car.sendMessageTCP(resposta.__str__())

    if car.visual:
        car.get_request()


def get_option_Serve_udp(car: Car) -> None:
    while car.__connected__:
        try:
            while car.is_continuo():
                msg: dict = {"success": True, "IP": car.ip, "descript": ""}

                if car.current_server_exe == car.server_option[2][0]:  # velocidade
                    msg["descript"] = f"Velocidade: {car.get_speed()}Km/h."
                elif car.current_server_exe == car.server_option[13][0]:  # status
                    msg["descript"] = f"Ficha Técnica: {car.get_status()}"
                elif car.current_server_exe == car.server_option[14][0]:  # gasolina
                    msg["descript"] = f"Gasolina: {car.gasoline}L"
                elif car.current_server_exe == car.server_option[15][0]:  # bateria
                    msg["descript"] = f"Bateria: {car.battery}%"
                elif car.current_server_exe == car.server_option[16][0]:  # Colisao
                    msg["descript"] = f"O sensor de colisão {'' if car.collision else 'não'} detectou uma colisão."
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
