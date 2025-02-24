import zmq
import json

from src.client.validator import data_validator


def send_data_to_server(command):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:8080")
    socket.send_json(command)
    response = socket.recv_json()
    return response


if __name__ == "__main__":
    data_request = str(input("Enter your json data to send to server: "))
    try:
        json_data = data_validator(data_request)
        send_data_to_server(json_data)
    except Exception as e:
        print({"error": str(e)})
