"""
Week 2 Programming Assignment: to_json decorator
"""


import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        result = json.dumps(result)
        return result
    return wrapped
        


@to_json
def get_data():
  return {
    'data': 42
  }
 
print(get_data())  # вернёт '{"data": 42}'

@to_json
def get_tuple():
    return tuple(("python", "json", "mysql"))
print(get_tuple())

@to_json
def get_int():
    return 4
print(get_int())