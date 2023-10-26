import socket
import logging
from src.infra.servers.server import Server


class TcpServer(Server):
  def __init__(
    self,
    bind_ip:str,
    bind_port:int,
    backlog=5,
    buffer_size=1024,
  ):
    logging.info("Starting TCP server...")
    super().__init__(bind_ip,bind_port,socket.SOCK_STREAM,backlog,buffer_size)