import os
import sys

import requests

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)
from config import HOST_HTTP


def get_report_error(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170
    NUM_BAR: int = 48

    print(get_paint_color("RED"), ('=-' * NUM_BAR).center(SIZE_CENTER_TEXT))
    print("ERRO!!!".center(SIZE_CENTER_TEXT + 1))
    print(text.center(SIZE_CENTER_TEXT))
    print(('=-' * NUM_BAR).center(SIZE_CENTER_TEXT + 3), get_paint_color())


def get_report_action(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170
    NUM_BAR: int = 48

    print(get_paint_color("GREEN"), ('=-' * NUM_BAR).center(SIZE_CENTER_TEXT))
    print("AÇÃO REALIZADA COM SUCESSO!!!".center(SIZE_CENTER_TEXT + 1))
    print(text.center(SIZE_CENTER_TEXT))
    print(('=-' * NUM_BAR).center(SIZE_CENTER_TEXT + 3), get_paint_color())


def get_paint_color(color: str = "WHITE") -> str:
    dict_color: dict[str, str] = {"RED": "\033[1;31m", "BLUE": "\033[1;34m", "YELLOW": "\033[1;33m",
                                  "GREEN": "\033[1;32m"}
    if color in dict_color:
        return dict_color[color]

    return "\033[1;97m"


def get_clear_prompt() -> None:
    if os.name == 'nt':
        os.system('cls') or None
    else:
        os.system('clear') or None


def get_baseboard() -> None:
    SIZE_CENTER: int = 170
    print(("-=" * 45).center(SIZE_CENTER - 2))


def print_device_options(ip: str) -> bool:
    try:
        dict_device = requests.get(f'{HOST_HTTP}/devices/{ip}')

        if dict_device.status_code != 200 and dict_device.status_code != 404:
            get_clear_prompt()
            get_report_error(dict_device.json()['descript'])
            return False
        elif dict_device.status_code == 404:
            get_clear_prompt()
            get_report_error("Dispositivo não encontrado.")
            return False

    except requests.exceptions.ConnectionError:
        get_clear_prompt()
        get_report_error("Erro ao conectar com o servidor.")
        return False

    cabecalho()
    topico("Dispositivo")
    get_baseboard()

    print(f"|{'Opções do Dispositivo: ' + dict_device.json()['ip']: ^86}|".center(168))
    print(f"|{('_' * 75): ^86}|".center(168))
    pular_linha(1)
    print(f"|{'Tipo de dispositivo: ' + dict_device.json()['tag'] + '      ' + 'Nome do dispositivo: '
              + dict_device.json()['name']: ^86}|".center(168))
    pular_linha(2)

    list_options = requests.get(f'{HOST_HTTP}/devices/{ip}/options').json()
    print_options_devices(list_options)

    pular_linha(2)
    get_baseboard()
    print(f"Digite [ {len(list_options) + 1} ] para voltar ao menu principal.".center(170))

    try:
        option = int(input((" " * 40) + "* Informe a opção desejada: ").replace(" ", ""))

        if option > len(list_options) + 1 or option < 1:
            get_clear_prompt()
            get_report_error("Opção inválida! Tente novamente.")
            return True
        elif option == len(list_options) + 1:
            get_clear_prompt()
            return False
        elif 'definir' in str(list_options[int(option) - 1][0]).replace("-", " "):
            value = input((" " * 40) + "* Informe o valor desejado: ").replace(" ", "")
            dict_option = requests.post(f'{HOST_HTTP}/devices/{ip}/{list_options[int(option) - 1][0]}/{value}')
        elif list_options[int(option) - 1][1]:
            dict_option = requests.post(f'{HOST_HTTP}/devices/{ip}/{list_options[int(option) - 1][0]}')
        else:
            dict_option = requests.get(f'{HOST_HTTP}/devices/{ip}/{list_options[int(option) - 1][0]}')

        get_clear_prompt()
        if dict_option.status_code == 200:
            get_report_action(dict_option.json()['descript'])
        else:
            get_report_error(dict_option.json()['descript'])

        return True
    except ValueError:
        get_clear_prompt()
        get_report_error("Opção inválida! Tente novamente.")
        return True


def print_options_devices(list_options: list[str]) -> None:

    text = ""
    for i in range(len(list_options)):
        text += f"{'[ ' + str(i + 1) + ' ] — ' + list_options[i][0].replace("-", " "): ^27}"
        if (i + 1) % 3 == 0:
            print(f"|{text: ^86}|".center(168))
            pular_linha(2)
            text = ""

    if text:
        print(f"|{text: ^86}|".center(168))


def cabecalho() -> None:
    get_baseboard()
    print(f"|{'Iot Controller': ^86}|".center(168))
    get_baseboard()
    print(("=-" * 25).center(168))
    print(("=-" * 15).center(168))


def topico(topico: str) -> None:
    print()
    print(f"=================== {topico: ^15} ===================".center(170))
    print()


def print_device_list() -> None:
    print("Conectando ao servidor...".center(170))
    get_clear_prompt()

    try:
        list_ips = requests.get(f'{HOST_HTTP}/devices').json()
    except requests.exceptions.ConnectionError:
        get_report_error("Erro ao conectar com o servidor.")
        return

    cabecalho()
    topico("Dispositivos")
    get_baseboard()

    pular_linha(1)
    print(f"|{'Quantidade de Dispositivos Conectados: ' + str(len(list_ips)): ^86}|".center(168))
    pular_linha(1)

    for ip_device in list_ips:
        dict_device: dict = requests.get(f'{HOST_HTTP}/devices/{ip_device}').json()

        print(f"|{('_' * 70): ^86}|".center(168))
        pular_linha(1)
        print(f"|{'Tipo de dispositivo: ' + dict_device['tag'] + '      ' + 'Nome do dispositivo: '
                  + dict_device['name']: ^86}|".center(168))
        print(f"|{'IP do dispositivo: ' + ip_device: ^86}|".center(168))
        pular_linha(1)
        print(f"|{('_' * 70): ^86}|".center(168))
        pular_linha(1)

    get_baseboard()
    print("Tecle ENTER para voltar ao menu principal.".center(170))
    input()
    get_clear_prompt()


def pular_linha(num: int) -> None:
    for i in range(num):
        print(f"|{'': ^86}|".center(168))


def get_display_option(num_option: str, name_option: str) -> None:
    SIZE_CENTER_TEXT: int = 170
    pular_linha(3)
    print(f"|{'[ ' + num_option + ' ] — ' + name_option: ^86}|".center(168))


def print_menu_main() -> None:
    print("\033[1;97m")
    cabecalho()

    topico("Menu Principal")
    get_baseboard()
    get_display_option("1", "Listar Dispositivos")
    get_display_option("2", "Acessar Dispositivo")
    get_display_option("3", "Encerrar Programa")

    pular_linha(3)
    get_baseboard()
