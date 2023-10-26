import socket
import sys
def main():
    host = '127.0.0.1'
    port = PORT = int(sys.argv[1]) 

    client_socket = socket.socket(type=socket.SOCK_STREAM)
    client_socket.connect((host, port))

    xml_data = """
    <request>
        <person>
            <name>Alice</name>
            <age>28</age>
        </person>
    </request>
    """

    client_socket.sendall(xml_data.encode('utf-8'))

    response = client_socket.recv(1024)
    print("Resposta do servidor:")
    print(response.decode('utf-8'))

    client_socket.close()

if __name__ == '__main__':
    main()