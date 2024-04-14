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
            msg = car.receiveMessage().lower()
            get_option_Serve(msg, car)
        except RuntimeError as e:
            break


def get_option_Serve(user_choice: str, car: Car) -> None:
    resposta: dict = {}
    try:
        if user_choice == "data":
            resposta = car.get_info()
    except RuntimeError:
        pass

    car.sendMessageTCP(resposta.__str__())

