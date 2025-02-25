import zmq
from src.utils.validator import data_validator
from src.utils.error_responses import ErrorResponse


def send_data_to_server(data):
    """ Send Client Data To Server """

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:8080")
    socket.send_json(data)
    response = socket.recv_json()
    return response


def get_data_from_client():
    """ Get Data From Client And Give One """
    while True:
        data_request = str(input("Enter your json data to send to server: "))
        try:
            json_data = data_validator(data_request)
            response = send_data_to_server(json_data)
            print(response)
        except Exception:
            print(ErrorResponse.OsOrCompute)



if __name__ == "__main__":
    get_data_from_client()


# { "command_type": "os", "command_name": "ping", "parameters": [ "1.1.1.1"] }