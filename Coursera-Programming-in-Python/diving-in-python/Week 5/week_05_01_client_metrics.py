import socket
import time 

class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.connection = socket.create_connection((self.host, self.port), self.timeout)

    def get(self, name):
        self.connection.sendall(f'get {name}\n'.encode('utf8'))
        answer = self._read()
        data = {} 
        if answer == '':
            return data

        for row in answer.split('\n'):
            try:
                name, value, timestamp = row.split()
                if name not in data:
                    data[name] = []
                data[name].append((int(timestamp), float(value)))
            except:
                raise ClientError()
        for k, v in data.items():
            v.sort()
        return data

    def put(self, name, value, timestamp=None):
        timestamp = timestamp or str(int(time.time()))
        self.connection.sendall(f'put {name} {value} {timestamp}\n'.encode('utf8'))
        self._read()

    def _read(self):
        data = b''
        while not data.endswith(b'\n\n'):
            data += self.connection.recv(1024)
        status, data = data.decode().split('\n', 1)
        if status != 'ok' or status == 'error':
            raise ClientError()
        data = data.strip()
        return data

class ClientError(socket.error):
	pass