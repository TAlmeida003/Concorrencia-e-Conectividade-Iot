import os
import sys

from Sensor import Sensor
import Serve
import User


def main() -> None:
    sensor = Sensor()
    Serve.iniciar_conexao(sensor)

    try:
        user_choice: int = User.get_main_manu_entry(sensor)

        while not User.is_exit_option(user_choice):
            User.get_option(user_choice, sensor)
            user_choice: int = User.get_main_manu_entry(sensor)

    except KeyboardInterrupt:
        sensor.end()
        return

    sensor.end()


if __name__ == '__main__':
    main()
