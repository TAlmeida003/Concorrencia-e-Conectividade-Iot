import socket
import threading
import time
from threading import Lock

HOST: str = socket.gethostbyname(socket.gethostname())
PORT_TCP: int = 5001
PORT_UDP: int = 5000


class Server:

    def __init__(self) -> None:
        self.__dictConnectDevices__: dict = {}

        self.__serve_udp__ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__serve_tcp__ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock: Lock = Lock()

    def connect_device(self) -> None:
        try:
            self.__serve_tcp__.bind((HOST, PORT_TCP))
            self.__serve_udp__.bind((HOST, PORT_UDP))

            self.__serve_tcp__.listen()
        except socket.error:
            raise RuntimeError("Servidor não foi inicializado.")

        print("Servidor online")
        print(f"Número de IP: {self.__serve_tcp__.getsockname()[0]} \n")
        threading.Thread(target=self.thread_connect_device).start()

    def thread_connect_device(self) -> None:
        while True:
            device_socket, addr = self.__serve_tcp__.accept()
            ip: str = str(device_socket.getpeername()[1])

            dict_device: dict = {"ip": ip, "socket": device_socket, "data_udp": {}, "opcoes": {}}
            self.__dictConnectDevices__[ip] = dict_device
            self.__dictConnectDevices__[ip]["opcoes"] = self.get_device_option(ip, "opcoes")["option"]

            threading.Thread(target=self.get_recv_udp, args=[ip]).start()

    def get_device_option(self, ip: str, option: str, value: str = "") -> dict:
        pack_msg: dict = {"option": option, "value": value}
        try:
            return self.get_dict(pack_msg.__str__(), ip)
        except KeyError:
            raise RuntimeError("Nao existe nenhum dispositivo com esse ip.")

    def get_dict(self, option: str, ip: str) -> dict:
        try:
            with self.lock:
                self.__dictConnectDevices__[ip]["socket"].send(option.encode())

                self.__dictConnectDevices__[ip]["socket"].settimeout(30)
                if self.is_command_utp(option, ip):
                    return eval(self.__dictConnectDevices__[ip]["socket"].recv(2048).decode('utf-8'))

                self.__dictConnectDevices__[ip]["flag_data"] = False
                while not self.__dictConnectDevices__[ip]["flag_data"]:
                    time.sleep(0.1)
                return self.__dictConnectDevices__[ip]["data_udp"]
        except socket.timeout:
            raise RuntimeError("Tempo limite de resposta excedido")
        except socket.error:
            self.__dictConnectDevices__[ip]["socket"].close()
            self.__dictConnectDevices__.pop(ip)
            raise RuntimeError("Nao foi possível acessar o dispositivo.")

    def get_recv_udp(self, ip: str) -> None:
        while True:
            try:
                data, addr = self.__serve_udp__.recvfrom(2048)
                data = data.decode()
                self.__dictConnectDevices__[ip]["data_udp"] = eval(data)
                self.__dictConnectDevices__[ip]["flag_data"] = True
            except socket.error:
                self.__dictConnectDevices__[ip]["socket"].close()
                self.__dictConnectDevices__.pop(ip)
                break

    def get_device(self, ip: str) -> dict:
        pack_msg: dict = {"option": "data", "value": ""}
        try:
            return self.get_dict(pack_msg.__str__(), ip)
        except KeyError:
            raise RuntimeError("Nao existe nenhum dispositivo com esse ip.")

    def get_list_devices(self) -> list:
        list_connect = []
        list_ip: list = list(self.__dictConnectDevices__.keys())
        for ip_device in list_ip:
            if self.is_connect(ip_device):
                list_connect.append(ip_device)
        return list_connect

    def is_connect(self, ip_device) -> bool:
        try:
            with self.lock:
                pack_msg: dict = {"option": "teste", "value": ""}
                self.__dictConnectDevices__[ip_device]["socket"].send(pack_msg.__str__().encode())
                self.__dictConnectDevices__[ip_device]["socket"].recv(2048)
                return True
        except socket.error:
            self.__dictConnectDevices__[ip_device]["socket"].close()
            self.__dictConnectDevices__.pop(ip_device)
            return False

    def end(self) -> None:
        self.__serve_tcp__.close()
        self.__serve_udp__.close()

    def is_command_utp(self, option: str, ip) -> bool:
        for i in self.__dictConnectDevices__[ip]["opcoes"]:
            if eval(option)["option"] == i[0] and (not i[1]):
                return False
        return True

    def get_list_options(self, ip: str) -> list:
        list_options: list = []
        try:
            for i in self.__dictConnectDevices__[ip]["opcoes"]:
                list_options.append((i[0], i[1]))
            return list_options
        except KeyError:
            raise RuntimeError("Nao existe nenhum dispositivo com esse ip.")

    def check_method_option(self, ip: str, option: str, method):
        try:
            for i in self.__dictConnectDevices__[ip]["opcoes"]:
                if option == i[0] and method != i[2]:
                    raise RuntimeError("Esta rota aceita apenas solicitações " + i[2])
                elif option == "data" or option == "teste" or option == "opcoes":
                    raise RuntimeError("Opção indisponíveis para o usuário.")
        except KeyError:
            raise RuntimeError("Nao existe nenhum dispositivo com esse ip.")
