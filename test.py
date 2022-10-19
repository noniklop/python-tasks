import socket

import requests
import threading

from urllib3.exceptions import MaxRetryError, NewConnectionError


def check_url(url):
    try:
        status_url = requests.get(url)
        print("Target: ", url)
        print("Status: ", status_url.ok, '\n')
    except (ConnectionError, MaxRetryError, NewConnectionError, socket.gaierror):
        status_url = False
        print("Target: ", url)
        print("Status: ", status_url, '\n')


t1 = threading.Thread(target=check_url('http://goog56le.com/'))
t2 = threading.Thread(target=check_url('https://wiki.python.org/moin/PythonBooks'))
t3 = threading.Thread(target=check_url('https://www.python.org/doc/av/'))

threads = (t1, t2, t3)

for t in threads:
    t.start()
for t in threads:
    t.join()
