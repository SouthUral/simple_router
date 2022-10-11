from pydoc import cli
import socket
from urllib import request, response


def parse_request(request):
    pass


def generate_response(request):
    method, url = parse_request(request)
    pass


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv()
        response = generate_response(request.decode('utf-8'))



if __name__ == '__main__':
    run()