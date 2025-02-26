import subprocess
from tabnanny import check


def execute_os_command(command_name, parameters, time_out=5):
    result = subprocess.check_output([command_name] + parameters,
                                     stderr=subprocess.STDOUT,
                                     shell=False,
                                     text=True,
                                     timeout=time_out
                                     )
    return result


def evaluate_math_expression(expression):
    result = eval(expression)
    return int(result)

