import subprocess
from tabnanny import check


def execute_os_command(command_name, parameters):
    execute_time_out = 5
    # todo: not
    result = subprocess.check_output([command_name] + parameters,
                                     stderr=subprocess.STDOUT,
                                     shell=False,
                                     text=True,
                                     )
    return result
    # except subprocess.CalledProcessError as e:
    #     return e.output
    # except subprocess.TimeoutExpired:
    #     return "Command timed out."
    # except Exception as e:
    #     return e
    # return result


def evaluate_math_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating math expression: {str(e)}"
