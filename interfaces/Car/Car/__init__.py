import socket

HOST: str = '192.168.25.107'
PORT_TCP: int = 5001
PORT_UDP: int = 5000


class Car:
    def __init__(self) -> None:
        self.modelo: str = "Toyota"
        self.marca: str = "Corolla"
        self.cor: str = "Preto"
        self.ano: int = 2022

        self.velocidade: int = 0
        self.state: bool = False
        self.connected: bool = False

        self.ip: str = socket.gethostbyname(socket.gethostname())
        self.server_option: list[str] = []
        self.exe_serve_atual: str = ""

        self.tcp_connection: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_connection: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connectBroker(self) -> None:
        # Conectar ao servidor broker
        try:
            if not self.connected:
                self.tcp_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tcp_connection.connect((HOST, PORT_TCP))
                self.connected = True
            else:
                raise RuntimeError("O broker já está conectado.")

        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Não foi possível conectar ao Broker.")

    def disconnectBroker(self) -> None:
        # Desconectar do servidor broker
        self.tcp_connection.close()
        self.connected = False

    def sendMessageUDP(self, data: str) -> None:
        # Enviar mensagem via UDP
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
        # Receber mensagem via TCP
        try:
            msg = self.tcp_connection.recv(2048).decode('utf-8')
            return msg
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def get_info(self) -> dict:
        return {"ip": self.ip,
                "modelo": self.modelo,
                "marca": self.marca,
                "cor": self.cor,
                "ano": self.ano,
                "opções": self.server_option
                }
