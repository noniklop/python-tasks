import requests
import threading


def check_url(url):
    try:
        status_url = requests.get(url)
        print("Target: ", url)
        print("Status: ", status_url.ok, '\n')
    except:
        status_url = False
        print("Target: ", url)
        print("Status: ", status_url, '\n')


t1 = threading.Thread(target=check_url('http://sphinx.pocoo.org/'))
t2 = threading.Thread(target=check_url('https://wiki.python.org/moin/PythonBooks'))
t3 = threading.Thread(target=check_url('https://www.python.org/doc/av/'))
t4 = threading.Thread(target=check_url('https://github.com/pallets/flask/tree/master/examples/tutorial/'))
t5 = threading.Thread(target=check_url('https://docs.python.org/3.5/'))
t6 = threading.Thread(target=check_url('https://pypi.org/project/Flask/0.5/'))
t7 = threading.Thread(target=check_url('https://psfmember.org/civicrm/contribute/transact'))
t8 = threading.Thread(target=check_url('https://github.com/pallets/flask'))
t9 = threading.Thread(target=check_url('https://wiki.python.org/moin/BeginnersGuide'))
t10 = threading.Thread(target=check_url('http://www.python.org/dev/peps/pep-0333/'))
t11 = threading.Thread(target=check_url('https://www.python.org/'))
t12 = threading.Thread(target=check_url('https://github.com/pallets/flask/issues'))
t13 = threading.Thread(target=check_url('https://www.python.org/dev/peps/'))
t14 = threading.Thread(target=check_url('https://github.com/pallets/flask-website'))
t15 = threading.Thread(target=check_url('https://www.python.org/'))
t16 = threading.Thread(target=check_url('https://github.com/pallets/flask'))
t17 = threading.Thread(target=check_url('http://jinja.pocoo.org/docs/'))
t18 = threading.Thread(target=check_url('http://lucumr.pocoo.org/'))
t19 = threading.Thread(target=check_url('https://www.python.org/doc/versions/'))
t20 = threading.Thread(target=check_url('https://www.does_not_exist.com/'))
t21 = threading.Thread(target=check_url('https://github.com/pallets/flask'))
t22 = threading.Thread(target=check_url('https://docs.python.org/3.6/'))
t23 = threading.Thread(target=check_url('https://pypi.org/project/Flask/1.0.2/'))
t24 = threading.Thread(target=check_url('https://docs.python.org/3.8/'))
t25 = threading.Thread(target=check_url('https://docs.python.org/2.7/'))
t26 = threading.Thread(target=check_url('https://docs.python.org/1.7/'))
t27 = threading.Thread(target=check_url('https://github.com/pallets/flask/issues'))


threads = (t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27)


for t in threads:
    t.start()
for t in threads:
    t.join()
