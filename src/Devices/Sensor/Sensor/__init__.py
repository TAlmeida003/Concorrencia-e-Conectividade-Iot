import os
import socket
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)

from ConnectionDevice import ConnectionDevice


class Sensor(ConnectionDevice):
    def __init__(self):
        # Inicialização dos atributos
        super().__init__()
        self.__temperature__: float = 0.0
        self.__humidity__: float = 0.0
        self.__state__: bool = False

        self.__name__: str = "SETNA00"
        self.__tag__: str = "sensor"
        self.__IP__: str = socket.gethostbyname(socket.gethostname())
        self.__server_options__: list[tuple[str, bool, str]] = [("ligar", True, "POST"),
                                                                ("desligar", True, "POST"),
                                                                ("temperatura-atual", False, "GET"),
                                                                ("umidade-atual", False, "GET"),
                                                                ("reiniciar", True, "POST"),
                                                                ("definir-nome", True, "POST")]
        self.__exe_serve_atual__: str = ""
        self.visual: bool = False
        self.exit: bool = False

    def turnOn(self) -> None:
        if self.__state__:
            raise RuntimeError("O sensor já está ligado.")
        self.__state__ = True

    def turnOff(self) -> None:
        if not self.__state__:
            raise RuntimeError("O sensor já está desligado.")

        self.__state__ = False

    def setTemperature(self, value: float) -> None:
        if not self.__state__:
            raise RuntimeError("O sensor está desligado.")
        elif value > 60:
            raise RuntimeError("Temperatura alta: limite de 60 ºC")
        elif 5 > value:
            raise RuntimeError("Temperatura baixa: limite de 5 ºC")
        self.__temperature__ = value

    def setHumidity(self, value: float) -> None:
        if not self.__state__:
            raise RuntimeError("O sensor está desligado.")
        elif value > 80:
            raise RuntimeError("umidade alta: limite de 80%")
        elif 20 > value:
            raise RuntimeError("umidade baixa: limite de 20%")
        self.__humidity__ = value

    def setName(self, name: str) -> None:
        if not name:
            raise RuntimeError("Nome invalido.")
        elif len(name) != 7:
            raise RuntimeError("Nome deve ter 7 caracteres")
        self.__name__ = name

    def restart(self) -> None:
        try:
            self.turnOff()
            self.turnOn()
        except RuntimeError:
            raise RuntimeError("Sensor não pode ser reiniciado.")

    def is_continuous_mod(self) -> bool:
        return ((self.__exe_serve_atual__ == self.__server_options__[2][0]) or
                (self.__exe_serve_atual__ == self.__server_options__[3][0]))

    def get_temperature(self) -> float:
        if not self.__state__:
            raise RuntimeError("Temperatura indisponível, sensor desligado.")
        return self.__temperature__

    def get_humidity(self) -> float:
        if not self.__state__:
            raise RuntimeError("Umidade indisponível, sensor desligado.")
        return self.__humidity__

    def set_option_serve(self, option: str) -> None:
        if not self.is_option(option) and option != "data" and option != "teste" and option != "opcoes":
            raise RuntimeError("opção invalida.")
        self.__exe_serve_atual__ = option

    def get_list_options(self) -> list:
        return self.__server_options__

    def is_option(self, option: str) -> bool:
        for i in self.__server_options__:
            if i[0] == option:
                return True
        return False

    def get_info(self) -> dict:
        # Obter informações do sensor
        return {"ip": self.__IP__,
                "name": self.__name__,
                "opções": self.__server_options__,
                "tag": self.__tag__
                }

    def end(self) -> None:
        self.exit = True
        self.disconnectBroker()