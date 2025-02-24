import logging
import zmq
from threading import Thread
from src.server.thread import handle_request

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()


def run_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:8080")
    logger.info("Server listening on port 8080 !")
    threads = []
    while True:
        thread = Thread(target=handle_request, args=(socket,))
        thread.start()
        threads.append(thread)


if __name__ == "__main__":
    run_server()