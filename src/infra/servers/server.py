import socket
import logging
from src.handlers.client_handler import ClientHandler


class Server:
  def __init__(
    self,
    bind_ip:str,
    bind_port:int,
    socket_type=socket.SOCK_STREAM,
    backlog=5,
    buffer_size=1024,
  ):
    self.bind_ip = bind_ip
    self.bind_port = bind_port
    self.backlog = backlog
    self.buffer_size = buffer_size
    self.socket_type = socket_type
    self.server = socket.socket(type=self.socket_type)
    
  def __bind_server(self):
    self.server.bind((self.bind_ip, self.bind_port))
    self.server.listen(self.backlog)
    logging.info(f"[*] Listening on {self.bind_ip}:{self.bind_port}")


  def __accept_connection(self):
    client, addr = self.server.accept()
    logging.info("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    client_handler = ClientHandler(client,addr, self.buffer_size)
    client_handler.start()

  def start(self):
    self.__bind_server()
    while True:
      self.__accept_connection()