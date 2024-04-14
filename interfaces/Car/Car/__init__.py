import socket

HOST: str = '192.168.25.107'
PORT_TCP: int = 5001
PORT_UDP: int = 5000


class Car:
    def __init__(self) -> None:
        self.model: str = "Toyota"
        self.brand: str = "Corolla"
        self.color: str = "Preto"
        self.year: int = 2022

        self.speed: int = 0
        self.state: bool = False
        self.connected: bool = False
        self.battery: int = 0
        self.gasoline: float = 0
        self.door_locked: bool = False
        self.direction: str = "parado"
        self.distance: int = 0
        self.moving: bool = False
        self.collision: bool = False

        self.ip: str = socket.gethostbyname(socket.gethostname())
        self.server_option: list[str] = []
        self.current_server_exe: str = ""

        self.tcp_connection: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_connection: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connectBroker(self) -> None:
        # Connect to broker server
        try:
            if not self.connected:
                self.tcp_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tcp_connection.connect((HOST, PORT_TCP))
                self.connected = True
            else:
                raise RuntimeError("Broker já conectado.")
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Falha ao conectar ao Broker.")

    def disconnectBroker(self) -> None:
        # Disconnect from broker server
        self.tcp_connection.close()
        self.connected = False

    def sendMessageUDP(self, data: str) -> None:
        # Send message via UDP
        try:
            self.udp_connection.sendto(data.encode('utf-8'), (HOST, PORT_UDP))
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def sendMessageTCP(self, data: str) -> None:
        try:
            self.tcp_connection.send(data.encode('utf-8'))
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def receiveMessage(self) -> str:
        # Receive message via TCP
        try:
            msg = self.tcp_connection.recv(2048).decode('utf-8')
            return msg
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def turnOn(self) -> None:
        # Ligar sensor
        if self.state:
            raise RuntimeError("O veículo já está ligado")
        elif self.battery == 0:
            raise RuntimeError("O veículo está sem bateria")
        elif self.gasoline == 0:
            raise RuntimeError("O veículo está sem gasolina")

        self.state = True

    def turnOff(self) -> None:
        # Desligar sensor
        if not self.state:
            raise RuntimeError("O veículo já está desligado")

        self.state = False

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
        self.door_locked = False

    def lock_door(self) -> None:
        if self.door_locked:
            raise RuntimeError("Porta já está travada")
        self.door_locked = True

    def go_forward(self) -> None:
        if self.direction == "frente":
            raise RuntimeError("O veículo já está indo para frente")
        elif not self.state:
            raise RuntimeError("O veículo só pode se mover ligado")
        elif self.battery == 0:
            raise RuntimeError("O veículo está sem bateria")
        elif self.gasoline == 0:
            raise RuntimeError("O veículo está sem gasolina")

        self.direction = "frente"

    def go_backward(self) -> None:
        if self.direction == "trás":
            raise RuntimeError("O veículo já está indo para trás")
        elif not self.state:
            raise RuntimeError("O veículo só pode se mover ligado")
        elif self.battery == 0:
            raise RuntimeError("O veículo está sem bateria")
        elif self.gasoline == 0:
            raise RuntimeError("O veículo está sem gasolina")

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

        self.speed = value

    def measure_distance(self):
        if not self.state:
            raise RuntimeError("O veículo não está ligado")
        elif not self.moving:
            raise RuntimeError("Inicie o movimento do carro")

        self.distance += self.speed

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

        self.moving = True

    def collision_detected(self) -> None:
        if self.collision:
            raise RuntimeError("O veículo já está em modo contra colisões")
        self.stop()
        self.collision = True

    def end_collision(self) -> None:
        if not self.collision:
            raise RuntimeError("O veículo não detectou nenhuma colisão")
        self.collision = False

    def get_info(self) -> dict:
        return {"ip": self.ip,
                "modelo": self.model,
                "marca": self.brand,
                "cor": self.color,
                "ano": self.year,
                "opções": self.server_option
                }
