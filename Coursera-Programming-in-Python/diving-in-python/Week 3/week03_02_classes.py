import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        fileext = os.path.splitext(self.photo_file_name)
        return fileext[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    car_type = 'car'

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try: 
            self.body_length, self.body_width, self.body_height = map(float, self.body_whl.split('x')) if self.body_whl else [0.0 for _ in range(3)]
        except ValueError:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    car_type = 'truck'

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.extra = extra

    car_type = 'spec_machine'

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            result = {}
            if len(row) != 7 or ('' in [row[0], row[1], row[3], row[5]]) or (row[0] not in ['car', 'truck', 'spec_machine']):
                item = None
            elif row[0] == 'car':
                try: 
                    item = Car(brand = row[1], passenger_seats_count = row[2], photo_file_name = row[3], carrying = row[5])
                except ValueError:
                    pass
            elif row[0] == 'truck':
                try:
                    item = Truck(brand = row[1], body_whl = row[4], photo_file_name = row[3], carrying = row[5])
                except ValueError:
                    pass   
            elif row[0] == 'spec_machine':
                if row[-1] == '':
                    item = None
                else:
                    try:
                        item = SpecMachine(brand = row[1], extra = row[-1], photo_file_name = row[3], carrying = row[5])
                    except ValueError:
                        pass
            if item != None and item.get_photo_file_ext() in ['.jpg', '.jpeg', '.png', '.gif']:
                car_list.append(item)
    return car_list