class ErrorResponse:
    OsOrCompute = {"error":"For command_type you can only choose os,compute."}
    LongRunning = {"error":"Long running command error."}
    JsonNeeded = {"error":"request data need to be json."}
    BadExpression = {"error":"Bad expression error."}