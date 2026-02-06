from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os


def hello_world(request):
    name = 'hello'
    if name is None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)


def create_app():
    """Application factory for gunicorn."""
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        return config.make_wsgi_app()


# WSGI app object for gunicorn
app = create_app()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    server = make_server('0.0.0.0', port, app)
    print(f"Serving on port {port}...")
    server.serve_forever()
