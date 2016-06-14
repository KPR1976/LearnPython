class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = 'good'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        print self.health

hippo = Animal("Joyse", 12, )
sloth = Animal("Roese", 13,)
ocelot = Animal("Ivan", 24,)

print hippo.health
print sloth.health
print ocelot.health
