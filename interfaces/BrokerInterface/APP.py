from flask import Flask, jsonify, request
from Serve import Serve

serve: Serve = Serve()
app = Flask(__name__)


# GET Listar dispositivos
# GET dispositivo
# GET listar opções do dispositivo
# GET opções ex.: temperatura

# PUT opções do dispositivo ex.: ligar


@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(serve.get_list_devices())


@app.route('/devices/<string:ip>', methods=['GET'])
def get_device(ip: str):
    try:
        return jsonify(serve.get_device(ip))
    except RuntimeError as e:
        return jsonify({"mensagem": e.__str__()}), 400


@app.route('/devices/<string:ip>/<string:opcao>', methods=['GET'])
def get_option_device(ip: str, opcao: str):
    try:
        return jsonify(serve.get_device_option(ip, opcao))
    except RuntimeError as e:
        return jsonify({"mensagem": e.__str__()}), 400


# @app.route('/devices/<string:ip>/<string:opcao>', methods=['PUT'])
# def put_option_device(ip: str, opcao: str):
#     try:
#         return jsonify(serve.get_device_option(ip, opcao))
#     except RuntimeError as e:
#         return jsonify({"mensagem": e.__str__()}), 400
