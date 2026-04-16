class MotorBike:

    # def __init__(self):
    #     print("empty constructor")

    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def __str__(self):
        return f'Gear: {self.gear}, Speed: {self.speed}'

# instance 1 or object 1
honda = MotorBike(4, 120)

# instance 2 or object 2
hero = MotorBike(4, 100)
print(honda)
print(hero)

activa = MotorBike()
print(activa)