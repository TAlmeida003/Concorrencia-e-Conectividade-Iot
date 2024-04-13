import requests

# Capaz de adm os dispositivos conectados
response = requests.get('http://172.16.103.13:2048/devices')
print(response.text)


def print_menu():
    print("\n ==== Menu Principal ==== \n")
    print("[ 1 ] - LISTAR DISPOSITIVOS CONECTADOS")
    print("[ 2 ] - OPÇÕES DO DISPOSITIVO")
    print("[ 3 ] - ENCERRAR PROGRAMA")

def main() -> None:
    pass


if __name__ == '__main__':
    main()
