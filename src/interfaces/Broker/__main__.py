import API


if __name__ == '__main__':
    try:
        API.serve.connect_device()
        API.app.run(port=5002, host='0.0.0.0')
    except RuntimeError as e:
        print(e.__str__())
    except KeyboardInterrupt:
        API.serve.end()
