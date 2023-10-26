import logging
from socket import socket
from threading import Thread
from src.utils.xml_parser import CustomXmlParser

class ClientHandler(Thread):
  def __init__(self, client:socket,addr, buffer_size=1024):
    super().__init__()
    self.client = client
    self.addr = addr
    self.buffer_size = buffer_size
    self.recv_data = b''
    self.proccesed_data:CustomXmlParser = None
    self.client.settimeout(10)
  
  def receive_data(self):
    logging.info("Receiving data")
    xml_data = b''
    while True:
      try:
        print(f"Receiving chunk, {self.buffer_size} bytes")
        chunk = self.client.recv(self.buffer_size)
        xml_data += chunk
        if len(chunk) < self.buffer_size:
          break
      except socket.timeout:
        logging.error("Timeout de recepção. Encerrando a conexão.")
        break
    if not xml_data:
      Exception("No data received")
    self.recv_data = xml_data
    print(self.recv_data)

  def client_close(self) -> None:
    logging.info("Closing client")
    self.client.close()

  def procces_data(self) -> None:
    self.proccesed_data = CustomXmlParser(self.data)

  def send_data(self,data:str) -> None:
    logging.info("Sending data")
    self.client.send(data.encode('utf-8'))

  def run(self) -> None:
    try:
      logging.info("Starting client handler")
      self.receive_data()
      self.send_data("OK")
      self.client_close()
      return
    except Exception as e:
      logging.error(e)
      self.send_data("ERROR")
      self.client_close()