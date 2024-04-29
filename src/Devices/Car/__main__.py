import os
import sys
from Car import Car
import Serve
import User

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import View


def main() -> None:
    View.get_clear_prompt()
    car: Car = Car()

    Serve.iniciar_conexao(car)

    try:
        user_choice: int = User.get_main_manu_entry(car)

        while not User.is_exit_option(user_choice):
            User.get_option(user_choice, car)
            user_choice: int = User.get_main_manu_entry(car)
    except KeyboardInterrupt:
        View.get_clear_prompt()
        car.disconnectBroker()
        return

    View.get_clear_prompt()
    car.disconnectBroker()


if __name__ == '__main__':
    main()
