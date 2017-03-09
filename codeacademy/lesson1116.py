class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        pass

    def check_angels(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
