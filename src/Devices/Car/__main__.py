from Car import Car
import Serve
import User


def main() -> None:
    car: Car = Car()
    Serve.start_connect(car)

    try:
        user_choice: int = User.get_main_manu_entry(car)

        while not User.is_exit_option(user_choice):
            User.get_option(user_choice, car)
            user_choice: int = User.get_main_manu_entry(car)

    except KeyboardInterrupt:
        car.end()
        return

    car.end()


if __name__ == '__main__':
    main()
