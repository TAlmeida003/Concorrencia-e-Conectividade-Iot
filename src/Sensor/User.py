import View
from Sensor import Sensor
import Serve


def is_exit_option(user_choice: int) -> bool:
    OPTION_EXIT: int = 8
    if user_choice != OPTION_EXIT:
        return False
    return True


def check_option_main_menu(user_choice: int) -> None:
    if user_choice < 1 or user_choice > 8:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: int) -> bool:
    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        View.get_report_error(error.__str__())
        return False


def display_main_menu(sensor: Sensor) -> None:
    conexao = "online" if sensor.__connected__ else "offline"
    state = "ligado" if sensor.__state__ else "desligado"
    temperatura = round(sensor.get_temperature(), 1).__str__() if sensor.__state__ else "-.-"
    umidade = round(sensor.get_humidity(), 1).__str__() if sensor.__state__ else "-.-"
    View.get_baseboard()
    print(f"| Dispositivo: Sensor       Nome: {sensor.__name__}          IP: {sensor.__IP__: ^15} |".center(170))
    print(f"| Broker: {conexao:^8}         Temperatura: {temperatura:^4}ºC       "
          f"   Umidade: {umidade: ^4}% |".center(170))
    print(f"| Estado do sensor: {state:^10} "
          f" Ultima requisição do broker: {sensor.__exe_serve_atual__:^9} |".center(170))
    View.get_baseboard()

    list_option: list[str] = ["LIGAR SENSOR", "DESLIGAR SENSOR", "CONECTAR AO BROKER", "DESCONECTAR DO BROKER",
                              "ALTERAR O NOME DO SENSOR", "MUDAR TEMPERATURA DO SENSOR",
                              "MUDAR UMIDADE DO SENSOR", "ENCERRAR PROGRAMA"]

    print("\n", (("=" * 15) + " MENU PRINCIPAL " + ("=" * 15)).center(170), "\n")
    View.get_baseboard()
    print()
    print(" " * 52, f"[ 1 ] - {list_option[0]:^9}               [ 2 ] - {list_option[1]:^9}", "\n" * 2)
    print(" " * 52, f"[ 3 ] - {list_option[2]:^9}         [ 4 ] - {list_option[3]:^9}", "\n" * 2)
    print(" " * 52, f"[ 5 ] - {list_option[4]:^9}   [ 6 ] - {list_option[5]:^9}", "\n" * 2)
    print(" " * 52, f"[ 7 ] - {list_option[6]:^9}    [ 8 ] - {list_option[7]:^9}", "\n" * 2)
    View.get_baseboard()
    print(" " * 52, "* INFORME QUAL A OPÇÃO DESEJADA: ", end="")


def input_main_menu_option(sensor: Sensor) -> int:
    try:
        display_main_menu(sensor)
        user_choice: int = int(input())
        return user_choice
    except ValueError:
        View.get_clear_prompt()
        return -1


def get_main_manu_entry(sensor: Sensor) -> int:
    user_choice: int = input_main_menu_option(sensor)

    while not is_a_valid_main_menu_option(user_choice):
        user_choice = input_main_menu_option(sensor)

    return user_choice


def get_option(user_choice: int, sensor: Sensor) -> None:
    try:
        if user_choice == 1:  # ligar
            sensor.turnOn()
        elif user_choice == 2:  # desligar
            sensor.turnOff()
        elif user_choice == 3:  # conectar
            Serve.iniciar_conexao(sensor)
        elif user_choice == 4:  # desconectar
            sensor.disconnectBroker()
        elif user_choice == 5:  # mudar nome
            print(" " * 52, "* INFORME O NOVO NOME DO SENSOR: ", end="")
            sensor.setName(input())
        elif user_choice == 6:  # mudar Temperatura
            try:
                print(" " * 52, "* INFORME A TEMPERATURA: ", end="")
                sensor.setTemperature(float(input()))
            except ValueError:
                raise RuntimeError("Campo destinado a números")
        elif user_choice == 7:  # Mudar Umidade
            try:
                print(" " * 52, "* INFORME A UMIDADE: ", end="")
                sensor.setHumidity(float(input()))
            except ValueError:
                raise RuntimeError("Campo destinado a números")
        View.get_clear_prompt()
    except RuntimeError as e:
        View.get_clear_prompt()
        View.get_report_error(e.__str__())
