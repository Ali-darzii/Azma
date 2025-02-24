from request import execute_os_command, evaluate_math_expression

def handle_request(socket):
    while True:
        message = socket.recv_json()
        command_type = message.get("command_type")

        if command_type == "os":
            command_name = message.get("command_name")
            parameters = message.get("parameters", [])
            try:
                result = execute_os_command(command_name, parameters)
            except Exception as e:
                pass

        elif command_type == "compute":
            expression = message.get("expression")
            result = evaluate_math_expression(expression)
        else:
            return socket.send_json({"error": "Invalid command type"})

        socket.send_json({"result": result})