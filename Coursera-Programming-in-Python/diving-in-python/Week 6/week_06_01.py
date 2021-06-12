import asyncio

storage = {}


def run_server(host, port):

    loop = asyncio.get_event_loop()
    coroutine = loop.create_server(ClientServerProtocol,host, port)
    server = loop.run_until_complete(coroutine)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        request = process_data(data.decode())
        self.transport.write(request.encode())


def process_data(data):
    try: 
        command, payload = data.split(' ', 1)
    except ValueError:
        return 'error\nwrong command\n\n'
    if command == 'put':
        result = put(payload)
        return result
    elif command == 'get':
        result = get(payload)
        return result
    else:
        return 'error\nwrong command\n\n'


def put(data):
    control = data.split()
    if len(control) != 3:
        return 'error\nwrong command\n\n'
    metric_name, metric_value, timestamp = data.split()
    try:
        if metric_name not in storage:
            storage[metric_name] = {}
            storage[metric_name].update({int(timestamp): float(metric_value)})
        else:
            storage[metric_name].update({int(timestamp): float(metric_value)})
    except ValueError:
        return 'error\nwrong command\n\n'
    return 'ok\n\n'


def get(data):
    control = data.split()
    if len(control) > 1:
        return 'error\nwrong command\n\n'
    key = data.strip()
    if key == '*':
        response = 'ok\n'
        for key, value in storage.items():
            for v in sorted(value):
                response += '{} {} {}\n'.format(key, value[v], v)
        response += '\n'
        return response
    elif key == '':
        return 'error\nwrong command\n\n'
    else:
        values = storage.get(key)
        if values:
            response = 'ok\n'
            for v in sorted(values):
                response += '{} {} {}\n'.format(key, values[v], v)
            response += '\n'
            return response
        else:
            return 'ok\n\n'


if __name__ == "__main__":
    run_server("127.0.0.1", 8888)
