import json

class StopException(Exception):
    response = None

def stop(response):
    e = StopException()
    e.response = response
    raise e

# middlewares
def actionHandler(nextStep, *args, **kwargs):
    try:
        response = nextStep()
    except StopException as e:
        response = e.response
    # complete response
    if not isinstance(response, tuple):
        response = (response, 200, {})
    else:
        if len(response) == 1:
            response = response + (200, {})
        elif len(response) == 2:
            response = response + ({},)
    # convert data to json if possible
    data = response[0]
    if isinstance(data, list) or isinstance(data, dict):
        response = list(response)
        response[0] = json.dumps(data)
        headers = response[2]
        headers['Content-Type'] = 'application/json'
        response = tuple(response)
    return response
