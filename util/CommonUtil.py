import json

def current_timestamp():
    import calendar;
    import time;
    ts = calendar.timegm(time.gmtime())
    return ts

def json_encode(data, status=True):
    response = {
        "success": status,
        "server_time": current_timestamp(),
        "response": data,
    }
    return response