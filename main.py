import logging
log = logging.getLogger()
try:
  import googleclouddebugger
  googleclouddebugger.enable()
except ImportError:
  log.exception()

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        message = request.args.get('message')
    elif request_json and 'message' in request_json:
        message = request_json['message']
    else:
        message = f'Hello World!'

    log.info("Received message: %s" % message)
    return message

