import os
import socket
import sys
import time

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)
from config import HOST, PORT_TCP, PORT_UDP


class ConnectionDevice:
    def __init__(self):
        self.__tcp_connection__: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__udp_connection__: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__connected__: bool = False
        self.user_connected: bool = False
        self.auto_connect: bool = False

    def connectBroker(self) -> None:
        # Conectar ao servidor broker
        try:
            if not self.__connected__:
                self.__tcp_connection__: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__tcp_connection__.connect((HOST, PORT_TCP))
                self.__tcp_connection__.send("add".encode())
                self.__connected__ = True
                self.user_connected: bool = True
            else:
                raise RuntimeError("O broker já está conectado.")
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Não foi possível conectar ao Broker.")

    def disconnectBroker(self) -> bool:
        # Desconectar do servidor broker
        if self.__connected__:
            self.__tcp_connection__.close()
            self.__connected__ = False
            return True
        return False

    def sendMessageUDP(self, data: str) -> None:
        if not self.__connected__:
            raise RuntimeError("Broker desconectado")

        try:
            self.__udp_connection__.sendto(data.encode('utf-8'), (HOST, PORT_UDP))
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def sendMessageTCP(self, data: str) -> None:
        if not self.__connected__:
            raise RuntimeError("Broker desconectado")

        try:
            self.__tcp_connection__.send(data.encode('utf-8'))
        except socket.error:
            self.disconnectBroker()
            raise RuntimeError("Broker desconectado")

    def receiveMessage(self) -> dict:
        if not self.__connected__:
            raise RuntimeError("Broker desconectado")

        while self.__connected__:
            try:
                self.__tcp_connection__.settimeout(5)
                msg: str = self.__tcp_connection__.recv(2048).decode('utf-8')
                if msg == "":
                    self.disconnectBroker()
                    raise RuntimeError("Broker desconectado")
                return eval(msg)
            except socket.timeout:
                if not self.is_connected_broker():
                    self.disconnectBroker()
                    raise RuntimeError("Broker desconectado")
            except socket.error:
                self.disconnectBroker()
                raise RuntimeError("Broker desconectado")

    def is_connected_broker(self) -> bool:
        try:
            tcp_aux: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_aux.connect((HOST, PORT_TCP))
            tcp_aux.send("aux".encode())
            tcp_aux.close()
            return True
        except OSError:
            return False

    def is_connection(self) -> bool:
        return self.__connected__

