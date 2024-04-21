import View


def main() -> None:
    try:
        View.print_menu_main()
        user_choice: str = input((" " * 40) + "* Informe a opção desejada: ")

        while not is_exit_option(user_choice):
            get_option(user_choice)
            View.print_menu_main()
            user_choice = input((" " * 40) + "* Informe a opção desejada: ")
    except KeyboardInterrupt:
        return


def is_exit_option(user_choice: str) -> bool:
    return user_choice == "3"


def get_option(user_choice: str) -> None:
    if user_choice == "1":
        View.get_clear_prompt()
        View.print_device_list()
    elif user_choice == "2":
        ip = input((" " * 40) + "* Informe o Endereço IP: ")
        View.get_clear_prompt()
        View.print_device_options(ip)
    else:
        View.get_clear_prompt()
        View.get_report_error("Opção inválida! Tente novamente.")


if __name__ == '__main__':
    main()
