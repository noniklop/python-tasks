Traceback (most recent call last):
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\util\connection.py", line 72, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\socket.py", line 954, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1040, in _send_output
    self.send(msg)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 980, in send
    self.connect()
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000002735355D7F0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='goog56le.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000002735355D7F0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Vladyslav_Melnychuk1\PycharmProjects\Part 4\test.py", line 20, in <module>
    t1 = threading.Thread(target=check_url('http://goog56le.com/'))
  File "C:\Users\Vladyslav_Melnychuk1\PycharmProjects\Part 4\test.py", line 11, in check_url
    status_url = requests.get(url)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Vladyslav_Melnychuk1\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='goog56le.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000002735355D7F0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

Process finished with exit code 1
