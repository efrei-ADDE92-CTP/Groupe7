import time
import random
import threading

import requests

def run():
    while True:
        try:
            requests.post(url="http://app:5000/predict", json= {'sepal_length': 0.1, 'sepal_width': 0.2, 'petal_length': 0.3, 'petal_width': 0.4},timeout=1)
        except:
            pass


if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.setDaemon(True)
        thread.start()

    while True:
        time.sleep(1)
