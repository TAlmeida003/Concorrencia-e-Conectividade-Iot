import APP


if __name__ == '__main__':
    try:
        APP.serve.connect_device()
        APP.app.run(port=2048, host='0.0.0.0')
    except RuntimeError as e:
        print(e.__str__())
    except KeyboardInterrupt:
        APP.serve.end()
