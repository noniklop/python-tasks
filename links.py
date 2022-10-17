import json

import requests
import threading


def check_url(url):
    status_url = requests.get(url)
    print("Target: ", url)
    print("Status: ", status_url.ok, '\n')


t1 = threading.Thread(target=check_url('https://google.com'))
t2 = threading.Thread(target=check_url('http://sphinx.pocoo.org/'))
t3 = threading.Thread(target=check_url('https://wiki.python.org/moin/PythonBooks'))

threads = (t1, t2, t3)
# check_url('https://google.com')

for t in threads:
    t.start()
for t in threads:
    t.join()
