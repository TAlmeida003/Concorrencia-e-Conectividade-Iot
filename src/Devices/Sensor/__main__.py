import os
import sys

from Sensor import Sensor
import Serve
import User

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import View


def main() -> None:
    View.get_clear_prompt()
    sensor = Sensor()
    Serve.iniciar_conexao(sensor)

    try:
        user_choice: int = User.get_main_manu_entry(sensor)

        while not User.is_exit_option(user_choice):
            User.get_option(user_choice, sensor)
            user_choice: int = User.get_main_manu_entry(sensor)

    except KeyboardInterrupt:
        sensor.disconnectBroker()

    sensor.disconnectBroker()


if __name__ == '__main__':
    main()
