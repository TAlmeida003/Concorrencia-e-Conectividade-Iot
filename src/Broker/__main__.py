import API
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)
from config import PORT_FLASK

if __name__ == '__main__':
    try:
        API.serve.connect_device()
        API.app.run(port=PORT_FLASK, host='0.0.0.0')
    except RuntimeError as e:
        print(e.__str__())
    except KeyboardInterrupt:
        API.serve.end()
