import logging
import socket
import threading

logging.basicConfig(filename="server.log",level=logging.INFO,format="%(asctime)s [%(levelname)s]: %(message)s")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.31.122"
port = 12345
server_socket.bind((host, port))
server_socket.listen()
client_connections = []
client_usernames = {}
def handle_client(client):
    try:
        client.send("Введите свое имя: ".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")
        while username in client_usernames:
            client.send("Имя пользователя уже занято!")
            username = client.recv(1024).decode("utf-8")
        client_usernames[client] = username
        broadcast(f"{username} connected")
        logging.info(f"{username} connected")
    except:
        remove(client)

def remove(client):
    if client in client_connections:
        client_connections.remove(client)
        username = client_usernames[client]
        del client_usernames[client]
        client.close()
        broadcast(f"{username} disconected")
        logging.info(f"{username} disconected")

def broadcast(message):
    for client in client_connections:
        try:
            client.send(message.encode("UTF-8"))
        except:
            remove(client)
