import subprocess
from src.server.manager import logger
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
        logger.info(f"Received: {data}")
        command_type = data.get("command_type")
        if command_type == "os":
            try:
                result = execute_os_command(data.get("command_name",[]), data.get("parameters",[]))
                socket.send_json({"result": result})
            except subprocess.TimeoutExpired:
                socket.send_json(ErrorResponse.LongRunning)
            except Exception as e:
                socket.send_json({"error": e})
        elif command_type == "compute":
            result = evaluate_math_expression(data.get("expression"))
            socket.send_json({"result": result})
        else:
            socket.send_json(ErrorResponse.OsOrCompute)

