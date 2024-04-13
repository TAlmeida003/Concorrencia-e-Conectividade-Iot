import os

def get_report_error(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170
    NUM_BAR: int = 40

    print(get_paint_color("RED"), ('=-' * NUM_BAR).center(SIZE_CENTER_TEXT))
    print("ERRO!!!".center(SIZE_CENTER_TEXT + 1))
    print(text.center(SIZE_CENTER_TEXT))
    print(('=-' * NUM_BAR).center(SIZE_CENTER_TEXT + 3), get_paint_color())


def get_clear_prompt() -> None:
    if os.name == 'nt':
        os.system('cls') or None
    else:
        os.system('clear') or None


def display_sub_title(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170
    NUM_BAR: int = 40

    print(get_paint_color("BLUE"))
    print(("=-" * NUM_BAR).center(SIZE_CENTER_TEXT + 2, " "))
    print(text.center(SIZE_CENTER_TEXT - 4))
    print(("=-" * NUM_BAR).center(SIZE_CENTER_TEXT + 2, " "))
    print(get_paint_color())


def display_header(text: str) -> None:
    SIZE_CENTER_TEXT: int = 170

    display_sub_title("LAMPADA")

    print(("= " * 23).center(SIZE_CENTER_TEXT - 2, " "))
    print((("==" * 10) + get_paint_color("BLUE") + " " + text + " "
           + get_paint_color() + ("==" * 10)).center(SIZE_CENTER_TEXT + 11))
    print(("= " * 20).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 15).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 5).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 3).center(SIZE_CENTER_TEXT, " "))


def get_baseboard() -> None:
    SIZE_CENTER: int = 170
    print(("-=" * 40).center(SIZE_CENTER))


def get_paint_color(color: str = "WHITE") -> str:
    dict_color: dict[str, str] = {"RED": "\033[1;31m", "BLUE": "\033[1;34m", "YELLOW": "\033[1;33m",
                                  "GREEN": "\033[1;32m"}
    if color in dict_color:
        return dict_color[color]

    return "\033[1;97m"


def get_display_option(color: str, num_option: str, name_option: str) -> None:
    SIZE_CENTER_TEXT: int = 170

    print(get_paint_color(color))
    print(f"[ {num_option} ] — {name_option}".center(SIZE_CENTER_TEXT))
    print(get_paint_color())