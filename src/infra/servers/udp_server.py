import socket
import logging
from src.infra.servers.server import Server


class UdpServer(Server):
  def __init__(
    self,
    bind_ip:str,
    bind_port:int,
    backlog=5,
    buffer_size=1024,
  ):
    logging.info("Starting UDP server...")
    super().__init__(bind_ip,bind_port,socket.AF_INET,backlog,buffer_size)