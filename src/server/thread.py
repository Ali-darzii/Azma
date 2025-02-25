from src.utils.error_responses import ErrorResponse
from src.server.controller  import execute_os_command, evaluate_math_expression
import zmq


def handle_request(worker_url, context: zmq.Context = None):
    """ Worker Routine """
    context = context or zmq.Context.instance()
    socket = context.socket(zmq.REP)
    socket.connect(worker_url)
    while True:
        data = socket.recv_json()
        command_type = data.get("command_type")
        if command_type == "os":
            result = execute_os_command(data.get("command_name",[]), data.get("parameters",[]))
            socket.send_json({"result": result})
        elif command_type == "compute":
            result = evaluate_math_expression(data)
            socket.send_json({"result": result})
        else:
            socket.send_json(ErrorResponse.OsOrCompute)

