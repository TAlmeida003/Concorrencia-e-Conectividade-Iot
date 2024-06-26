import os
import sys
import threading
from Car import Car
import Serve

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
import View


def is_exit_option(user_choice: int) -> bool:
    return user_choice == 18


def check_option_main_menu(user_choice: int) -> None:
    if 1 > user_choice or user_choice > 19:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: int) -> bool:
    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        View.get_clear_prompt()
        View.get_report_error(error.__str__())
        return False


def display_main_menu(car: Car) -> None:
    conexao = "Online" if car.__connected__ else "Offline"
    state = "Ligado" if car.state else "Desligado"
    porta = "Travada" if car.door_locked else "Destravada"
    movimento = "Ativa" if car.moving else "Desativado"
    colisao = "Detectada" if car.moving else "--------"

    View.get_baseboard()
    print(f"| Dispositivo: Carro           Modelo: {car.__model__}           IP: {car.ip: ^15} |".center(170))
    print(f"| Broker: {conexao: ^8}     Velocidade: {car.speed: ^3}Km/h      Estado do carro: {state: ^10} |"
          f"".center(170))
    print(f"| Marca: {car.__brand__}                  Cor: {car.color: ^5}                      Ano: {car.year: ^4} |"
          f"".center(170))
    print(
        f"| Bateria: {car.battery: ^3}%             Gasolina: {round(car.gasoline, 1):^4}L               Porta: {porta: ^10} "
        f"|".center(170))
    print(
        f"| Distancia: {round(car.distance, 2).__str__() + ' m': ^12}     Direção: {car.direction: ^7}    Movimentação: "
        f"{movimento :^11} |".center(170))
    print(f"| Colisão: {colisao: ^9}                 Ultima requisição do broker: {car.current_server_exe: ^9} |"
          f"".center(170))

    View.get_baseboard()
    print("\n", (("=" * 15) + " MENU PRINCIPAL " + ("=" * 15)).center(170), "\n")
    View.get_baseboard()
    print()

    list_options: list[str] = ["LIGAR VEÍCULO", "DESLIGAR VEÍCULO", "CONECTAR AO BROKER", "DESCONECTAR DO BROKER",
                              "DEFINIR VELOCIDADE", "DEFINIR BATERIA", "DEFINIR GASOLINA", "TRAVAR PORTA",
                              "DESTRAVAR PORTA", "DEFINIR DIREÇÃO PARA FRENTE", "INICIAR MOVIMENTO", "PARAR VEÍCULO",
                              "DEFINIR DIREÇÃO PARA TRÁS", "ATIVAR SENSOR DE COLISÃO", "DESATIVA SENSOR DE COLISÃO",
                              "ATIVA BUZINA", "DESATIVAR BUZINA", "ENCERRAR PROGRAMA"]
    for i in range(1, len(list_options), 3):
        print(f"[ {i: ^1} ] - {list_options[i - 1]:^26}        [ {i + 1:^1} ] - {list_options[i]:^26}        "
              f"[ {i + 2: ^1} ] - {list_options[i + 1]: ^26}".center(170), "\n" * 1)
    View.get_baseboard()

    print(f"Digite [ {len(list_options) + 1} ] para ver dados recebidos pelo servidor.".center(170))
    print(" " * 41, "* INFORME QUAL A OPÇÃO DESEJADA: ", end="")


def input_main_menu_option(car: Car) -> int:
    try:
        display_main_menu(car)
        user_choice: int = int(input())
        return user_choice
    except ValueError:
        View.get_clear_prompt()
        return -1


def get_main_manu_entry(car: Car) -> int:
    user_choice: int = input_main_menu_option(car)

    while not is_a_valid_main_menu_option(user_choice):
        user_choice = input_main_menu_option(car)

    return user_choice


def get_option(user_choice: int, car: Car) -> None:
    try:
        if user_choice == 1:  # LIGAR VEÍCULO
            car.turnOn()
        elif user_choice == 2:  # DESLIGAR VEÍCULO
            car.turnOff()
        elif user_choice == 3:  # CONECTAR AO BROKER
            Serve.start_connect(car)
            return
        elif user_choice == 4:  # DESCONECTAR DO BROKER
            if car.disconnectBroker():
                car.user_connected = False
            else:
                raise RuntimeError("Veículo não está conectado.")
        elif user_choice == 5:  # DEFINIR VELOCIDADE
            try:
                print(" " * 41, "* INFORME A VELOCIDADE: ", end="")
                car.set_speed(int(input()))
            except ValueError:
                raise RuntimeError("Campo destinado a números inteiros.")
        elif user_choice == 6:  # DEFINIR BATERIA
            try:
                print(" " * 41, "* INFORME A BATERIA: ", end="")
                car.set_battery(int(input()))
            except ValueError:
                raise RuntimeError("Campo destinado a números inteiros.")
        elif user_choice == 7:  # DEFINIR GASOLINA
            try:
                print(" " * 41, "* INFORME A GASOLINA: ", end="")
                car.set_gasoline(float(input()))
            except ValueError:
                raise RuntimeError("Campo destinado a números.")
        elif user_choice == 8:  # TRAVAR PORTA
            car.lock_door()
        elif user_choice == 9:  # DESTRAVAR PORTA
            car.unlock_door()
        elif user_choice == 10:  # DEFINIR DIREÇÃO PARA FRENTE
            car.go_forward()
        elif user_choice == 11:  # INICIAR MOVIMENTO
            car.start_movement()
        elif user_choice == 12:  # PARAR VEÍCULO
            car.stop()
        elif user_choice == 13:  # DEFINIR DIREÇÃO PARA TRAS
            car.go_backward()
        elif user_choice == 14:  # ATIVAR SENSOR DE COLISÃO
            car.collision_detected()
        elif user_choice == 15:  # DESATIVAR SENSOR DE COLISÃO
            car.end_collision()
        elif user_choice == 16:  # ATIVA BUZINA
            car.on_buzzer()
        elif user_choice == 17:  # DESATIVAR BUZINA
            car.off_buzzer()
        elif user_choice == 19:
            car.visual = True
            car.get_request()
            input()
            car.visual = False

        View.get_clear_prompt()
    except RuntimeError as e:
        View.get_clear_prompt()
        View.get_report_error(e.__str__())



