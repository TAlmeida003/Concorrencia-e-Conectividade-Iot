import socket

HOST: str = '192.168.0.104'
PORT_TCP: int = 5001
PORT_UDP: int = 5000


class Sensor:
    def __init__(self):
        # Inicialização dos atributos
        self.__temperature__: float = 0.0
        self.__humidity__: float = 0.0
        self.__state__: bool = False

        # Atributos de conexão
        self.__connected__: bool = False
        self.__name__: str = "SETNA05"
        self.__IP__: str = socket.gethostbyname(socket.gethostname())
        self.__server_options__: list[str] = ["ligar", "desligar", "temperatura-atual", "umidade-atual",
                                              "reiniciar"]
        self.__exe_serve_atual__: str = ""

        # Inicialização das conexões TCP e UDP
        self.__tcp_connection__: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__udp_connection__: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connectBroker(self) -> None:
        # Conectar ao servidor broker
        try:
            if not self.__connected__:
                self.__tcp_connection__: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #self.__udp_connection__: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.__tcp_connection__.connect((HOST, PORT_TCP))
                self.__connected__ = True
            else:
                raise RuntimeError("O broker já está conectado.")

        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Não foi possível conectar ao Broker.")

    def disconnectBroker(self) -> None:
        # Desconectar do servidor broker
        self.__tcp_connection__.close()
        self.__connected__ = False

    def sendMessageUDP(self, data: str) -> None:
        # Enviar mensagem via UDP
        try:
            self.__udp_connection__.sendto(data.encode('utf-8'), (HOST, PORT_UDP))
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def sendMessageTCP(self, data: str) -> None:
        try:
            self.__tcp_connection__.send(data.encode('utf-8'))
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def receiveMessage(self) -> str:
        # Receber mensagem via TCP
        try:
            msg = self.__tcp_connection__.recv(2048).decode('utf-8')
            return msg
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def turnOn(self) -> None:
        # Ligar sensor
        if self.__state__:
            raise RuntimeError("O sensor já está ligado.")
        self.__state__ = True

    def turnOff(self) -> None:
        # Desligar sensor
        if not self.__state__:
            raise RuntimeError("O sensor já está desligado.")

        self.__state__ = False

    def setTemperature(self, value: float) -> None:
        # Definir temperatura
        if not self.__state__:
            raise RuntimeError("O sensor está desligado.")
        elif value > 60:
            raise RuntimeError("Temperatura alta: limite de 60 ºC")
        elif 5 > value:
            raise RuntimeError("Temperatura baixa: limite de 5 ºC")
        self.__temperature__ = value

    def setHumidity(self, value: float) -> None:
        # Definir umidade
        if not self.__state__:
            raise RuntimeError("O sensor está desligado.")
        elif value > 80:
            raise RuntimeError("umidade alta: limite de 80%")
        elif 20 > value:
            raise RuntimeError("umidade baixa: limite de 20%")
        self.__humidity__ = value

    def setName(self, name: str) -> None:
        # Definir nome do sensor
        if not name:
            raise RuntimeError("Nome invalido.")
        elif len(name) != 7:
            raise RuntimeError("Nome deve ter 7 caracteres")

        self.__name__ = name

    def restart(self) -> None:
        try:
            self.turnOff()
            self.turnOn()
        except RuntimeError as e:
            raise RuntimeError("Sensor não pode ser reiniciado.")

    def get_exe_option(self) -> str:
        return self.__exe_serve_atual__

    def is_continuous_mod(self) -> bool:
        return ((self.__exe_serve_atual__ == self.__server_options__[2]) or
                (self.__exe_serve_atual__ == self.__server_options__[3]))

    def get_temperature(self) -> float:
        if not self.__state__:
            raise RuntimeError("Temperatura indisponível, sensor desligado.")
        return self.__temperature__

    def get_humidity(self) -> float:
        if not self.__state__:
            raise RuntimeError("Umidade indisponível, sensor desligado.")
        return self.__humidity__

    def set_option_serve(self, option: str) -> None:
        if (option not in self.__server_options__) and option != "data" and option != "teste":
            raise RuntimeError("opção invalida.")
        if not ((option == self.__server_options__[2]) or (option == self.__server_options__[3]) or option == "teste"):
            self.__exe_serve_atual__ = option
        elif self.__exe_serve_atual__ == self.__server_options__[2] and option == self.__server_options__[3]:
            self.__exe_serve_atual__ = option
        elif self.__exe_serve_atual__ == self.__server_options__[3] and option == self.__server_options__[2]:
            self.__exe_serve_atual__ = option

    def get_list_options(self) -> list:
        return self.__server_options__

    def get_info(self) -> dict:
        # Obter informações do sensor
        return {"IP": self.__IP__,
                "nome": self.__name__,
                "opções": self.__server_options__,
                }
