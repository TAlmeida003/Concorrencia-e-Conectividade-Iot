import socket
import threading

HOST: str = socket.gethostbyname(socket.gethostname())
PORT_TCP: int = 5001
PORT_UDP: int = 5000


class Serve:
    def __init__(self) -> None:
        self.dictConnectDevices: dict = {}

        self.serve_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serve_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_device(self) -> None:
        try:
            self.serve_tcp.bind((HOST, PORT_TCP))
            self.serve_udp.bind((HOST, PORT_UDP))

            self.serve_tcp.listen()
        except socket.error:
            raise RuntimeError("Servidor não foi inicializado.")
        print("Servidor online")
        print(f"Número de IP: {self.serve_tcp.getsockname()[0]} \n")

        threading.Thread(target=self.thread_connect_device).start()

    def thread_connect_device(self) -> None:
        while True:
            device_socket, addr = self.serve_tcp.accept()
            ip: str = device_socket.getpeername()[0]
            dict_device: dict = {"ip": ip, "socket": device_socket, "data_udp": {}}

            self.dictConnectDevices[ip] = dict_device

            threading.Thread(target=self.get_recv_udp, args=[device_socket.getpeername()[0]]).start()

    def get_device_option(self, ip: str, option: str) -> dict:
        try:
            return self.get_dict(option, ip)
        except KeyError:
            raise RuntimeError("Nao existe nenhum dispositivo com esse ip.")

    def get_dict(self, option: str, ip: str) -> dict:
        try:
            self.dictConnectDevices[ip]["socket"].send(option.encode())
            self.dictConnectDevices[ip]["socket"].settimeout(1)
            return eval(self.dictConnectDevices[ip]["socket"].recv(2048).decode('utf-8'))
        except socket.timeout:
            return self.dictConnectDevices[ip]["data_udp"]
        except socket.error:
            self.dictConnectDevices[ip]["socket"].close()
            self.dictConnectDevices.pop(ip)
            raise RuntimeError("Nao foi possível acessar o dispositivo.")

    def get_recv_udp(self, ip: str) -> None:
        while True:
            try:
                data, addr = self.serve_udp.recvfrom(2048)
                data = data.decode()
                self.dictConnectDevices[ip]["data_udp"] = eval(data)
            except socket.error:
                self.dictConnectDevices[ip]["socket"].close()
                self.dictConnectDevices.pop(ip)
                break

    def get_device(self, ip: str) -> dict:
        try:
            return self.get_dict("data", ip)
        except KeyError:
            raise RuntimeError("Nao existe nenhum dispositivo com esse ip.")

    def get_list_devices(self) -> list:
        list_connect = []
        list_ip: list = list(self.dictConnectDevices.keys())
        for ip_device in list_ip:
            if self.is_connect(ip_device):
                list_connect.append(ip_device)
        return list_connect

    def is_connect(self, ip_device) -> bool:
        try:
            self.dictConnectDevices[ip_device]["socket"].send("teste".encode())
            return True
        except socket.error:
            self.dictConnectDevices[ip_device]["socket"].close()
            self.dictConnectDevices.pop(ip_device)
            return False
