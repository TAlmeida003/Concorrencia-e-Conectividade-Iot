import threading
import Screen
from Car import Car


def iniciar_conexao(car: Car) -> None:
    print("conectando ao servidor...".center(170))
    try:
        car.connectBroker()
        threading.Thread(target=receive_and_respond, args=[car]).start()
        Screen.get_clear_prompt()
    except RuntimeError as e:
        Screen.get_clear_prompt()
        Screen.get_report_error(e.__str__())


def receive_and_respond(car: Car) -> None:
    while True:
        try:
            msg: dict = eval(car.receiveMessage())
            get_option_Serve(msg, car)
        except RuntimeError as e:
            break


def get_option_Serve(pack_msg: dict , car: Car) -> None:
    resposta: dict = {"success": True, "IP": car.ip, "descript": ""}
    try:
        if pack_msg["option"] == "data":
            resposta = car.get_info()
        elif pack_msg["option"] == "teste":
            return

    except RuntimeError as e:
        resposta = {"success": False, "code": 400, "message": e.__str__()}

    car.sendMessageTCP(resposta.__str__())

