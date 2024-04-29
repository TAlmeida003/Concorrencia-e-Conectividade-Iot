import os
import socket
import sys
import threading
import time

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)
from ConnectionDevice import ConnectionDevice


class Car(ConnectionDevice):
    def __init__(self) -> None:
        super().__init__()
        self.__model__: str = "Toyota"
        self.__brand__: str = "Corolla"
        self.color: str = "Preto"
        self.year: int = 2022
        self.tag: str = "carro"
        self.name: str = "CARTN05"

        self.speed: int = 0
        self.state: bool = False
        self.battery: int = 100
        self.gasoline: float = 22
        self.door_locked: bool = False
        self.direction: str = "parado"
        self.distance: float = 0
        self.moving: bool = False
        self.collision: bool = False

        self.ip: str = socket.gethostbyname(socket.gethostname())
        self.server_option: list[tuple[str, bool, str]] = [("ligar", True, "POST"), ("desligar", True, "POST"),
                                                           ("get-velocidade", False, "GET"),
                                                           ("definir-velocidade", True, "POST"),
                                                           ("travar-porta", True, "POST"),
                                                           ("destravar-porta", True, "POST"),
                                                           ("ir-para-frente", True, "POST"),
                                                           ("ir-para-tras", True, "POST"),
                                                           ("parar", True, "POST"),
                                                           ("iniciar-movimento", True, "POST"),
                                                           ("ativa-buzina", True, "POST"),
                                                           ("desativar-buzina", True, "POST"),
                                                           ("medir-distancia", False, "GET"),
                                                           ("status", False, "GET")]
        self.current_server_exe: str = ""

    def turnOn(self) -> None:
        # Ligar sensor
        if self.state:
            raise RuntimeError("O veículo já está ligado")
        elif self.battery == 0:
            raise RuntimeError("O veículo está sem bateria")

        self.state = True

    def turnOff(self) -> None:
        # Desligar sensor
        if not self.state:
            raise RuntimeError("O veículo já está desligado")
        elif self.moving:
            raise RuntimeError("O carro não pode ser desligado em movimento")

        self.state = False
        self.distance = 0
        self.direction = "parado"

    def set_battery(self, value: int) -> None:
        if value < 0 or value > 100:
            raise RuntimeError("Valor inválido para a bateria")
        self.battery = value

    def set_gasoline(self, value: float):
        if value < 0 or value > 55:
            raise RuntimeError("Valor inválido para a gasolina")
        self.gasoline = value

    def unlock_door(self) -> None:
        if not self.door_locked:
            raise RuntimeError("Porta já está destravada")
        elif self.state:
            raise RuntimeError("Não é possível destravar a porta com o veículo ligado")

        self.door_locked = False

    def lock_door(self) -> None:
        if self.door_locked:
            raise RuntimeError("Porta já está travada")
        elif self.state:
            raise RuntimeError("Não é possível travar a porta com o veículo ligado")

        self.door_locked = True

    def go_forward(self) -> None:
        if self.direction == "frente":
            raise RuntimeError("O veículo já está indo para frente")
        elif self.moving:
            raise RuntimeError("Não é possível definir a direção com o veículo em movimento")
        elif self.battery == 0:
            raise RuntimeError("O veículo está sem bateria")
        elif self.gasoline == 0:
            raise RuntimeError("O veículo está sem gasolina")
        elif not self.state:
            raise RuntimeError("O veículo está desligado")

        self.direction = "frente"

    def go_backward(self) -> None:
        if self.direction == "trás":
            raise RuntimeError("O veículo já está indo para trás")
        elif self.moving:
            raise RuntimeError("Não é possível definir a direção com o veículo em movimento")
        elif self.battery == 0:
            raise RuntimeError("O veículo está sem bateria")
        elif self.gasoline == 0:
            raise RuntimeError("O veículo está sem gasolina")
        elif not self.state:
            raise RuntimeError("O veículo está desligado")

        self.direction = "trás"

    def stop(self) -> None:
        if self.direction == "parado":
            raise RuntimeError("O veículo já está parado")

        self.distance = 0
        self.moving = False
        self.direction = "parado"

    def set_speed(self, value: int) -> None:
        if value < 0 or value > 220:
            raise RuntimeError("Velocidade inválida")
        elif not self.state:
            raise RuntimeError("O veículo está desligado")

        self.speed = value

    def measure_distance(self):
        while self.moving and self.__connected__:
            speed_ms = self.speed * 1000 / 3600
            if self.direction == "frente":
                self.distance += speed_ms
            else:
                self.distance -= speed_ms
            time.sleep(1)
        if self.__connected__:
            self.stop()

    def start_movement(self) -> None:
        if self.moving:
            raise RuntimeError("O veículo já está em movimento")
        elif self.direction == "parado":
            raise RuntimeError("É necessário dá sentido ao veículo")
        elif self.collision:
            raise RuntimeError("Possível colisão detectada")
        elif not self.state:
            raise RuntimeError("O veículo só pode se mover ligado")
        elif self.battery == 0:
            raise RuntimeError("O veículo está sem bateria")
        elif self.gasoline == 0:
            raise RuntimeError("O veículo está sem gasolina")
        elif self.speed == 0:
            raise RuntimeError("O veículo não pode se mover sem velocidade")

        self.moving = True
        threading.Thread(target=self.measure_distance).start()

    def collision_detected(self) -> None:
        if self.collision:
            raise RuntimeError("O veículo já está em modo contra colisões")
        self.stop()
        self.collision = True

    def end_collision(self) -> None:
        if not self.collision:
            raise RuntimeError("O veículo não detectou nenhuma colisão")
        self.collision = False

    def set_option(self, option: str) -> None:
        if not self.is_option(option) and option != "data" and option != "teste" and option != "opcoes":
            raise RuntimeError("Opção invalida")
        self.current_server_exe = option

    def is_option(self, option: str) -> bool:
        for i in self.server_option:
            if i[0] == option:
                return True
        return False

    def is_continuo(self) -> bool:
        return (self.current_server_exe == self.server_option[2][0]) or \
                (self.current_server_exe == self.server_option[12][0]) or \
                (self.current_server_exe == self.server_option[13][0])

    def get_info(self) -> dict:
        return {"ip": self.ip,
                "name": self.name,
                "tag": self.tag,
                "opções": self.server_option
                }

    def get_list_options(self):
        return self.server_option

    def get_speed(self) -> int:
        if not self.state:
            raise RuntimeError("O veículo está desligado")
        return self.speed

    def get_distance(self) -> float:
        if not self.state:
            raise RuntimeError("O veículo está desligado")
        elif not self.moving:
            raise RuntimeError("O veículo não está em movimento")
        return self.distance

    def get_status(self) -> dict:
        return {"modelo": self.__model__,
                "marca": self.__brand__,
                "cor": self.color,
                "ano": self.year,
                "estado": "Ligado" if self.state else "Desligado",
                "bateria": self.battery,
                "gasolina": self.gasoline,
                "porta": "Travada" if self.door_locked else "Destravada",
                "direcao": self.direction,
                "movimento": "Em movimento" if self.moving else "Parado",
                "colisao": "Detectada" if self.collision else "Não detectada"
                }