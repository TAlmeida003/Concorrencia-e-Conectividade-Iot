def is_exit_option(user_choice: int) -> bool:
    OPTION_EXIT: int = 8

    if user_choice != OPTION_EXIT:
        return False
    return True


def check_option_main_menu(user_choice: int) -> None:
    set_option: set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

    if user_choice not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: int) -> bool:
    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        Screen.get_report_error(error.__str__())
        return False


def display_main_menu() -> None:
    list_option: list[str] = ["LIGAR", "DESLIGAR", "CONECTAR", "DESCONECTAR", "NOME DO APARELHO", "MUDAR TEMPERATURA",
                              "MUDAR UMIDADE", "ENCERRAR"]

    print("\n ===== MENU PRINCIPAL ====\n")

    for i in range(len(list_option)):
        print(f"[{i + 1}] - {list_option[i]}")


def input_main_menu_option() -> int:
    try:
        display_main_menu()
        user_choice: int = int(input("INFORME QUAL A OPÇÃO DESEJADA: "))
        Screen.get_clear_prompt()
        return user_choice
    except ValueError:
        Screen.get_clear_prompt()
        return -1


def get_main_manu_entry() -> int:
    user_choice: int = input_main_menu_option()

    while not is_a_valid_main_menu_option(user_choice):
        user_choice = input_main_menu_option()

    return user_choice


def get_option(user_choice: int, sensor: Sensor) -> None:
    pass
