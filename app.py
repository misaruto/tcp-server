import os
import logging
from src.infra.logs.custom_json_formatter import CustomJsonFormatter
from src.infra.servers.tcp_server import TcpServer

APP_NAME = "tcp-server"

file_dir = os.path.split(os.path.realpath(__file__))[0]
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
formatter = CustomJsonFormatter("%(timestamp)s %(levelname)s %(message)s", json_ensure_ascii=False)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

loggerFile = logging.FileHandler(f"{file_dir}/{APP_NAME}.log")
loggerFile.setFormatter(formatter)
logger.addHandler(loggerFile)

logger.info("Starting server...")

server = TcpServer("0.0.0.0", 9999)
server.start()