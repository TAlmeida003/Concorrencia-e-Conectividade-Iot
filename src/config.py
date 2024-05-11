import os

# Dispositivos e portas de comunicação do sistema
HOST: str = os.getenv('HOST', '172.16.103.1')  # IP do servidor
PORT_TCP: int = 5001  # Porta de comunicação TCP
PORT_UDP: int = 5000  # Porta de comunicação UDP

# Servidor Flask e endereço de acesso
HOST_FLASK: str = '0.0.0.0'  # IP do servidor Flask
PORT_FLASK: int = 5002  # Porta de comunicação do servidor Flask
HOST_HTTP: str = f'http://{HOST}:{PORT_FLASK}'  # Endereço de acesso ao servidor Flask
