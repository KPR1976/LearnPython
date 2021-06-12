import os
import tempfile
import random

class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

        if not os.path.exists(self.path_to_file):
            open(self.path_to_file, 'w').close()


    def read(self):
        with open(self.path_to_file, 'r')  as f:
            result = f.read()
        return result
    

    def write(self, item):
        with open(self.path_to_file, 'w')  as f:
            f.write(item)

    def __str__(self):
        return self.path_to_file
    
    def __add__(self, other):
        new_file_name = 'file' + str(random.randint(0, 10))
        new_file_path = os.path.join(tempfile.gettempdir(), new_file_name)
        new_file_obj = File(new_file_path)
        new_file_obj.write(self.read() + other.read())
        return new_file_obj

    def __iter__(self):
        with open(self.path_to_file) as f:
            for line in f:
                yield line
