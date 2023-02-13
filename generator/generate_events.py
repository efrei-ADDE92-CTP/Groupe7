import time
import random
import threading

import requests

def run():
    while True:
        try:
            requests.post(url="http://127.0.0.1:5000/predict", json= {'sepal_length': 0.1, 'sepal_width': 0.2, 'petal_length': 0.3, 'petal_width': 0.4},timeout=1)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    while True:
        run()