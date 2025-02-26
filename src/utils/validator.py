import json


def data_validator(data_request):
    json_data = json.loads(data_request)

    command_type = json_data.get("command_type")
    if command_type != "os" and command_type != "compute":
        raise ValueError("Invalid command type")

    return json_data