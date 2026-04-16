class Animal(object):
    def __init__(self, name):
        self.name = name
    def fly(self):
        print('flying')


animal = Animal('Animal')
animal.fly()
