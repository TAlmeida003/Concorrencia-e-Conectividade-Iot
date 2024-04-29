# Dispositivos e portas de comunicação do sistema
HOST: str = '192.168.0.104'
PORT_TCP: int = 5001
PORT_UDP: int = 5000

# Servidor Flask e endereço de acesso
HOST_FLASK: str = '0.0.0.0'
PORT_FLASK: int = 5002
HOST_HTTP: str = f'http://{HOST}:{PORT_FLASK}'
