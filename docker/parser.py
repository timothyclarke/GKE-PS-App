#!/usr/bin/env python
import os
import os.path
import socket
import requests
import json
from sys import getsizeof

IP    = "0.0.0.0"
PORT  = 8080
SOCKET_TIMEOUT = 0.2

def fetch_content(tryCount = 5):
  headers   = { 'Accept': 'application/json'}
  nextTry = tryCount - 1
  try:
    response  = requests.get(url="https://reqres.in/api/products/", headers=headers)
  except Exception as e:
    if tryCount > 1:
      response = fetch_content(nextTry)
    else:
      print("Call to reqres.in had errors")
      print(e)
  if response.status_code > 200 and tryCount > 1:
    response = fetch_content(nextTry)
  return response.json()

def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    if resource == '/healthz':
        http_header = "HTTP/1.0 200 OK\r\n"
        http_header += "Content-Type: text/html; charset=utf-8\r\n"
        data = "Healthy\r\n"
        http_header += "Content-Length:" + str(len(data)) + "\r\n"
        http_response = http_header + "\r\n" + data
        client_socket.send(http_response.encode())
    else:
        data = fetch_content()
        http_header = "HTTP/1.0 200 OK\r\n"
        http_header += "Content-Type: application/json\r\n"
        json_content = json.dumps(data)
        http_header += "Content-Length:" + str(len(json_content)) + "\r\n"
        http_response = http_header + "\r\n" + json_content
        client_socket.send(http_response.encode())


def validate_http_request(request):
    """ Check if request is a valid HTTP request and returns TRUE / FALSE   and the requested URL """
    request_li = request.split("\r\n")[0].split(" ")
    if request_li[0] != "GET" or request_li[2] != "HTTP/1.1":
        return False, ''
    return True, request_li[1]

def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    #print('Client connected')
    try:
        while True:
            client_request = client_socket.recv(1024).decode('utf8')
            print(client_request.split("\r\n")[0])
            valid_http, resource = validate_http_request(client_request)
            if valid_http:
                #print('Got a valid HTTP request')
                handle_client_request(resource, client_socket)
            else:
                if len(client_request) > 0:
                    print("Error: HTTP request isn't valid")
                break
        #print("closing connection")
        client_socket.close()
    except socket.timeout:
        #print("closing connections")
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(10)
    print("Listening for connections on port %d" % PORT)

    while True:
        client_socket, client_address = server_socket.accept()
        client_socket.settimeout(SOCKET_TIMEOUT)
        #print('New connection received')
        handle_client(client_socket)

if __name__ == "__main__":
    main()
