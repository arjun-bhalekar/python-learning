class LandAnimal:
    def walk(self):
        print('walk')

class WaterAnimal:
    def swim(self):
        print('swim')

class AmphibianAnimal(LandAnimal, WaterAnimal):
    pass

frog = AmphibianAnimal()
print(frog.walk())
print(frog.swim())