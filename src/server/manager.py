import logging
import zmq
from threading import Thread


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()


def run_server():
    """ Server Routine """
    from src.server.thread import handle_request

    url_worker = "inproc://workers"
    url_client = "tcp://*:8080"
    number_of_workers = 5

    context = zmq.Context.instance()
    clients = context.socket(zmq.ROUTER)
    clients.bind(url_client)
    logger.info("Server listening on port 8080!")

    workers = context.socket(zmq.DEALER)
    workers.bind(url_worker)

    for i in range(number_of_workers):
        thread = Thread(target=handle_request, args=(url_worker,))
        thread.daemon = True
        thread.start()
        logger.info(f"Worker {i} started ...")

    zmq.proxy(clients, workers)

    # for sake of clean code
    clients.close()
    workers.close()
    context.term()
    logger.info("Server terminated!")




if __name__ == "__main__":
    run_server()