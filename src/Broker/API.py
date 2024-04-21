"""
API em Python Flask para gerenciar dispositivos e suas opções.

Este script fornece uma API RESTful construída com Flask para interagir com dispositivos e gerenciar suas opções.

Endpoints:
    - GET /devices: Obter uma lista de dispositivos.
    - GET /devices/<ip>: Obter informações sobre um dispositivo específico.
    - GET /devices/<ip>/options: Obter uma lista de opções disponíveis para um dispositivo específico.
    - GET /devices/<ip>/<option>: Obter o valor de uma opção específica para um dispositivo.
    - POST /devices/<ip>/<option>: Definir o valor de uma opção específica para um dispositivo.
    - POST /devices/<ip>/<option>/<value>: Definir o valor de uma opção específica para um dispositivo.

Autor: Thiago Neri dos Santos Almeida
Data: 20-04-2024
"""

from flask import Flask, jsonify, request
from Server import Server

serve: Server = Server()
app = Flask(__name__)


@app.route('/devices', methods=['GET'])  # GET Listar dispositivos
def get_devices():
    """
    Obter uma lista de dispositivos.

    Retorna:
        JSON: Uma resposta JSON contendo a lista de dispositivos.
       """
    if request.method != 'GET':
        return jsonify({"success": False, "descript": "Esta rota aceita apenas solicitações GET"}), 405

    return jsonify(serve.get_list_devices())


@app.route('/devices/<string:ip>', methods=['GET'])  # GET dispositivo
def get_device(ip: str):
    """
        Obter informações sobre um dispositivo específico identificado pelo seu endereço IP.

        Parâmetros:
            ip (str): O endereço IP do dispositivo.

        Retorna:
            JSON: Uma resposta JSON contendo informações sobre o dispositivo.
        """
    if request.method != 'GET':
        return jsonify({"success": False, "descript": "Esta rota aceita apenas solicitações GET"}), 405

    try:
        return jsonify(serve.get_device(ip))
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400


@app.route('/devices/<string:ip>/options', methods=['GET'])  # GET listar opções do dispositivo
def get_options_device(ip: str):
    """
        Obter uma lista de opções disponíveis para um dispositivo específico identificado pelo seu endereço IP.

        Parâmetros:
            ip (str): O endereço IP do dispositivo.

        Retorna:
            JSON: Uma resposta JSON contendo a lista de opções para o dispositivo.
        """
    if request.method != 'GET':
        return jsonify({"success": False, "descript": "Esta rota aceita apenas solicitações GET"}), 405

    try:
        return jsonify(serve.get_list_options(ip))
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400


@app.route('/devices/<string:ip>/<string:option>', methods=['GET'])
def get_option_device(ip: str, option: str):
    """
        Obter o valor de uma opção específica para um dispositivo identificado pelo seu endereço IP.

        Parâmetros:
            ip (str): O endereço IP do dispositivo.
            option (str): A opção a ser obtida.

        Retorna:
            JSON: Uma resposta JSON contendo o valor da opção solicitada.
        """
    try:
        serve.check_method_option(ip, option, request.method)
        dict_resp: dict = serve.get_device_option(ip, option)
        if not dict_resp["success"]:
            return jsonify(dict_resp), dict_resp["code"]
        return jsonify(dict_resp)
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400


@app.route('/devices/<string:ip>/<string:option>', methods=['POST'])
def post_option_device(ip: str, option: str):
    """
    Define uma opção específica para um dispositivo identificado pelo seu endereço IP.

    Parâmetros:
        ip (str): O endereço IP do dispositivo.
        option (str): A opção a ser definida.

    Retorna:
        JSON: Uma resposta JSON confirmando o sucesso da operação.
    """
    try:
        serve.check_method_option(ip, option, request.method)
        dict_resp: dict = serve.get_device_option(ip, option)
        if not dict_resp["success"]:
            return jsonify(dict_resp), dict_resp["code"]
        return jsonify(dict_resp)
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400


@app.route('/devices/<string:ip>/<string:option>/<string:value>', methods=['POST'])
def post_option_device_value(ip: str, option: str, value: str):
    """
    Define o valor de uma opção específica para um dispositivo identificado pelo seu endereço IP.

    Parâmetros:
        ip (str): O endereço IP do dispositivo.
        option (str): A opção a ser definida.
        value (str): O valor a ser definido para a opção.

    Retorna:
        JSON: Uma resposta JSON confirmando o sucesso da operação.
    """
    try:
        serve.check_method_option(ip, option, request.method)

        dict_resp: dict = serve.get_device_option(ip, option, value)
        if not dict_resp["success"]:
            return jsonify(dict_resp), dict_resp["code"]
        return jsonify(dict_resp)
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400
