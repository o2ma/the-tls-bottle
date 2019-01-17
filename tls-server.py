import bottle
from bottle import route, run, Response
from gevent import monkey; monkey.patch_all()
 
app = bottle.default_app()
 
@route('/')
def index():
    """Returns standard text response to show app is working."""
    return Response("My Bottle app is up and running!")
 
 
if __name__ == '__main__':
	run(host='0.0.0.0', port=5000, reloader=False, interval=10, server='gevent', certfile='server.crt', keyfile='server.key')