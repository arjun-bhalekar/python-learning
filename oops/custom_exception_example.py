# 1.define custom Exception class
class LowFuelError(Exception):
    pass

# 2.throw custom exception if condition meets
def start_car(fuel_level):
    if fuel_level <= 10:
        # manually trigger error or exception
        raise LowFuelError(f"Fuel is too low ({fuel_level}). Please refuel !")
    print('Engine Started !')

# 3.Handling of custom exception
try:
    start_car(19)
except LowFuelError as e:
    print(f"Error caught : {e}")
else:
    print('Have a good day!')