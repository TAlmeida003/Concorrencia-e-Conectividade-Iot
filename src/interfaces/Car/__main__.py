from Car import Car
import Serve
import Screen
import User


def main() -> None:
    Screen.get_clear_prompt()
    car: Car = Car()

    Serve.iniciar_conexao(car)

    try:
        user_choice: int = User.get_main_manu_entry(car)

        while not User.is_exit_option(user_choice):
            User.get_option(user_choice, car)
            user_choice: int = User.get_main_manu_entry(car)
    except KeyboardInterrupt:
        Screen.get_clear_prompt()
        car.disconnectBroker()
        return

    Screen.get_clear_prompt()
    car.disconnectBroker()


if __name__ == '__main__':
    main()
