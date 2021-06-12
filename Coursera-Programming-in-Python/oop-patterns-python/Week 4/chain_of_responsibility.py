class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ''


class EventGet:
    def __init__(self, kind):
        self.kind = kind
        self.value = None


class EventSet:
    def __init__(self, value):
        self.kind = type(value)
        self.value = value


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, _obj, event):
        if self.__successor is not None:
            return self.__successor.handle(_obj, event)


class IntHandler(NullHandler):
    def handle(self, _obj, event):
        if event.kind == int and event.value is not None:
            _obj.integer_field = event.value
            return _obj.integer_field
        elif event.kind == int and event.value is None:
            return _obj.integer_field
        else:
            return super().handle(_obj, event)


class FloatHandler(NullHandler):
    def handle(self, _obj, event):
        if event.kind == float and event.value is not None:
            _obj.float_field = event.value
            return _obj.float_field
        elif event.kind == float and event.value is None:
            return _obj.float_field
        else:
            return super().handle(_obj, event)


class StrHandler(NullHandler):
    def handle(self, _obj, event):
        if event.kind == str and event.value is not None:
            _obj.string_field = event.value
            return _obj.string_field
        elif event.kind == str and event.value is None:
            return _obj.string_field
        else:
            return super().handle(_obj, event)

if __name__ == '__main__':
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
    obj = SomeObject()

    chain.handle(obj, EventGet(int))
    chain.handle(obj, EventGet(str))
    chain.handle(obj, EventGet(float))
    chain.handle(obj, EventSet(1))
    chain.handle(obj, EventSet(1.1))
    chain.handle(obj, EventSet("str"))