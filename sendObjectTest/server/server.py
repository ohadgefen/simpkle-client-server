import socket
import time
import pickle # do ser

HEADERSIZE = 10
NUMBER_OF_MAX_LISTENER = 5
class Server():

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# IPV4 , TCP
        self.s.bind((socket.gethostname(),1236))# IP,port

    # ------------------------------------------------------------------------------------------------------------------
    def start_server(self):
        self.s.listen(NUMBER_OF_MAX_LISTENER)

        while(True):
            client_socket, address = self.s.accept()
            print(f"Connection from {address} has been established!")

            d = {1: "Hey", 2: "There"}
            msg = pickle.dumps(d)  # like serialized in java (convert to bytes)
            msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

            client_socket.send(msg)


if __name__ == "__main__":
    mServer = Server()
    mServer.start_server()