from flask import Flask, jsonify, request
from Server import Server

serve: Server = Server()
app = Flask(__name__)


@app.route('/devices', methods=['GET'])  # GET Listar dispositivos
def get_devices():
    if request.method != 'GET':
        return jsonify({"success": False, "descript": "Esta rota aceita apenas solicitações GET"}), 405
    return jsonify(serve.get_list_devices())


@app.route('/', methods=['GET'])  # GET Listar dispositivos
def get_home():
    return "<h1>API de gerenciamento de dispositivos</h1>"


@app.route('/devices/<string:ip>', methods=['GET'])  # GET dispositivo
def get_device(ip: str):
    if request.method != 'GET':
        return jsonify({"success": False, "descript": "Esta rota aceita apenas solicitações GET"}), 405

    try:
        return jsonify(serve.get_device(ip))
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400


@app.route('/devices/<string:ip>/options', methods=['GET'])  # GET listar opções do dispositivo
def get_options_device(ip: str):
    if request.method != 'GET':
        return jsonify({"success": False, "descript": "Esta rota aceita apenas solicitações GET"}), 405

    try:
        return jsonify(serve.get_list_options(ip))
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400


@app.route('/devices/<string:ip>/<string:option>', methods=['GET'])
def get_option_device(ip: str, option: str):
    return get_device_aux(ip, option)


@app.route('/devices/<string:ip>/<string:option>', methods=['POST'])
def post_option_device(ip: str, option: str):
    return get_device_aux(ip, option)


@app.route('/devices/<string:ip>/<string:option>/<string:value>', methods=['POST'])
def post_option_device_value(ip: str, option: str, value: str):
    return get_device_aux(ip, option, value)


def get_device_aux(ip: str, option: str, value: str = None):
    try:
        serve.check_method_option(ip, option, request.method)

        if value:
            dict_resp: dict = serve.get_device_option(ip, option, value)
        else:
            dict_resp: dict = serve.get_device_option(ip, option)

        if not dict_resp["success"]:
            return jsonify(dict_resp), dict_resp["code"]
        return jsonify(dict_resp)
    except RuntimeError as e:
        return jsonify({"success": False, "descript": e.__str__()}), 400