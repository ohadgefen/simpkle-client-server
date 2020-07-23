import socket
import time
import pickle # do ser

HEADERSIZE = 10
BUFFER_SIZE = 16


class Client():

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# IPV4 , TCP

    # ------------------------------------------------------------------------------------------------------------------
    def start_client(self):

        self.s.connect((socket.gethostname(),1236))# IP,port

        while(True):

            full_msg = b''
            new_msg = True

            while(True):
                msg = self.s.recv(BUFFER_SIZE)

                if(new_msg):
                    print(f"new message length: {msg[:HEADERSIZE]}")
                    msglen = int(msg[:HEADERSIZE])
                    new_msg = False

                full_msg += msg

                if(len(full_msg) - HEADERSIZE == msglen):
                    print("full message recvd")
                    print(full_msg[HEADERSIZE:])

                    d = pickle.loads(full_msg[HEADERSIZE:])
                    print(d)
                    new_msg = True
                    full_msg = b''

            print(full_msg)


if __name__ == "__main__":
    mClient = Client()
    mClient.start_client()