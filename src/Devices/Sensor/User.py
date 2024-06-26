import os
import sys
import threading

from Sensor import Sensor
import Serve

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import View


def is_exit_option(user_choice: int) -> bool:
    return user_choice == 8


def check_option_main_menu(user_choice: int) -> None:
    if user_choice < 1 or user_choice > 9:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: int) -> bool:
    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        View.get_clear_prompt()
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

    list_options: list[str] = ["LIGAR SENSOR", "DESLIGAR SENSOR", "CONECTAR AO BROKER", "DESCONECTAR DO BROKER",
                               "ALTERAR O NOME DO SENSOR", "MUDAR TEMPERATURA DO SENSOR",
                               "MUDAR UMIDADE DO SENSOR", "ENCERRAR PROGRAMA"]

    print("\n", (("=" * 15) + " MENU PRINCIPAL " + ("=" * 15)).center(170), "\n")
    View.get_baseboard()
    print()
    print(" " * 52, f"[ 1 ] - {list_options[0]:^9}               [ 2 ] - {list_options[1]:^9}", "\n" * 2)
    print(" " * 52, f"[ 3 ] - {list_options[2]:^9}         [ 4 ] - {list_options[3]:^9}", "\n" * 2)
    print(" " * 52, f"[ 5 ] - {list_options[4]:^9}   [ 6 ] - {list_options[5]:^9}", "\n" * 2)
    print(" " * 52, f"[ 7 ] - {list_options[6]:^9}    [ 8 ] - {list_options[7]:^9}", "\n" * 2)
    View.get_baseboard()

    print(f"Digite [ {len(list_options) + 1} ] para ver dados recebidos pelo servidor.".center(170))
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
            return
        elif user_choice == 4:  # desconectar
            if sensor.disconnectBroker():
                sensor.user_connected = False
            else:
                raise RuntimeError("Sensor não está conectado.")
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
        elif user_choice == 9:
            sensor.visual = True
            get_request(sensor)
            input()
            sensor.visual = False

        View.get_clear_prompt()
    except RuntimeError as e:
        View.get_clear_prompt()
        View.get_report_error(e.__str__())


def get_request(sensor: Sensor):
    View.get_clear_prompt()
    conexao = "online" if sensor.__connected__ else "offline"
    state = "ligado" if sensor.__state__ else "desligado"
    udp = "ativado" if (sensor.is_continuous_mod() and sensor.__connected__) else "desativado"
    temperatura = round(sensor.get_temperature(), 1).__str__() if sensor.__state__ else "-.-"
    umidade = round(sensor.get_humidity(), 1).__str__() if sensor.__state__ else "-.-"

    View.get_baseboard()
    print("\n", (("=" * 15) + " DADOS RECEBIDOS DO SERVIDOR " + ("=" * 15)).center(170), "\n")
    print()

    View.get_baseboard()
    print(f"|{'Requisição': ^16}|{'Nome': ^16}|{'Estado': ^16}|{'Conexão': ^16}|{'UDP Dados': ^16}|".center(170))
    View.get_baseboard()
    print(f"|{sensor.__exe_serve_atual__:^16}|{sensor.__name__:^16}|{state:^16}|"
          f"{conexao:^16}|{udp:^16}|".center(170))
    View.get_baseboard()
    print()

    View.get_baseboard()
    print(f"|{'Temperatura': ^16}|{'Umidade': ^16}|{'IP': ^16}|".center(170))
    View.get_baseboard()
    print(f"|{temperatura:^16}|{umidade:^16}|{sensor.__IP__: ^16}|".center(170))
    View.get_baseboard()
    print()

    View.get_baseboard()
    print(f"Lista de Threads - Threads ativas: {threading.active_count()} ".center(170))
    View.get_baseboard()
    txt: str = ""
    for thread in threading.enumerate():
        txt += f"|{thread.name: ^22}|"
    print(txt.center(170))
    View.get_baseboard()

    print("\n" * 2)
    print(f"Digite ENTER para voltar ao menu principal.".center(170))
