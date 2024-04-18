from flask import Flask, jsonify, request
from Server import Server

serve: Server = Server()
app = Flask(__name__)


@app.route('/devices', methods=['GET'])  # GET Listar dispositivos
def get_devices():
    if request.method != 'GET':
        return jsonify({"mensagem": "Esta rota aceita apenas solicitações GET"}), 405
    return jsonify(serve.get_list_devices())


@app.route('/devices/<string:ip>', methods=['GET'])  # GET dispositivo
def get_device(ip: str):
    if request.method != 'GET':
        return jsonify({"mensagem": "Esta rota aceita apenas solicitações GET"}), 405

    try:
        return jsonify(serve.get_device(ip))
    except RuntimeError as e:
        return jsonify({"mensagem": e.__str__()}), 400


@app.route('/devices/<string:ip>/opcoes', methods=['GET'])  # GET listar opções do dispositivo
def get_options_device(ip: str):
    if request.method != 'GET':
        return jsonify({"mensagem": "Esta rota aceita apenas solicitações GET"}), 405

    try:
        return jsonify(serve.get_list_options(ip))
    except RuntimeError as e:
        return jsonify({"mensagem": e.__str__()}), 400


@app.route('/devices/<string:ip>/<string:opcao>', methods=['GET'])  # GET listar opções do dispositivo
def get_option_device(ip: str, opcao: str):
    try:
        serve.check_method_option(ip, opcao, request.method)
        dict_resp: dict = serve.get_device_option(ip, opcao)
        if not dict_resp["success"]:
            return jsonify(dict_resp), dict_resp["code"]
        return jsonify(dict_resp)
    except RuntimeError as e:
        return jsonify({"mensagem": e.__str__()}), 400


@app.route('/devices/<string:ip>/<string:opcao>', methods=['POST'])  # GET opções ex.: ligar
def put_option_device(ip: str, opcao: str):
    try:
        serve.check_method_option(ip, opcao, request.method)
        dict_resp: dict = serve.get_device_option(ip, opcao)
        if not dict_resp["success"]:
            return jsonify(dict_resp), dict_resp["code"]
        return jsonify(dict_resp)
    except RuntimeError as e:
        return jsonify({"mensagem": e.__str__()}), 400


# PUT opções do dispositivo ex.: ligar
@app.route('/devices/<string:ip>/<string:opcao>/<string:value>', methods=['POST'])  # GET opções ex.: temperatura
def put_option_device_value(ip: str, opcao: str, value: str):
    try:
        serve.check_method_option(ip, opcao, request.method)

        dict_resp: dict = serve.get_device_option(ip, opcao, value)
        if not dict_resp["success"]:
            return jsonify(dict_resp), dict_resp["code"]
        return jsonify(dict_resp)
    except RuntimeError as e:
        return jsonify({"mensagem": e.__str__()}), 400
