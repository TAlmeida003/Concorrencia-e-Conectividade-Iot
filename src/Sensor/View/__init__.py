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


def get_baseboard() -> None:
    SIZE_CENTER: int = 170
    print(("-=" * 40).center(SIZE_CENTER))


def get_paint_color(color: str = "WHITE") -> str:
    dict_color: dict[str, str] = {"RED": "\033[1;31m", "BLUE": "\033[1;34m", "YELLOW": "\033[1;33m",
                                  "GREEN": "\033[1;32m"}
    if color in dict_color:
        return dict_color[color]

    return "\033[1;97m"
