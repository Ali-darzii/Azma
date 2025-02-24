import subprocess


def execute_os_command(command_name, parameters):
    result = subprocess.check_output([command_name] + parameters, stderr=subprocess.STDOUT, shell=True, text=True)
    return result

# Function to evaluate math expressions
def evaluate_math_expression(expression):
    try:
        # Safe evaluation of the expression using eval
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating math expression: {str(e)}"