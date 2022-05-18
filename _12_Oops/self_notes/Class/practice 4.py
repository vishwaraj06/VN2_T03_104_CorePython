class Vehicle:
    vehicle_type="Two Wheeler"
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full:')

    def drive(self):
        print(f'The {self.model} is now Ready.')

    @classmethod
    def our_class(cls):
        print("vehicle Type:",Vehicle.vehicle_type)

vehicle_object = Vehicle('Honda', 'Ridgeline', 'Truck')
Vehicle.our_class()
print(vehicle_object.brand)
print(vehicle_object.model)
print(vehicle_object.type)
vehicle_object.fuel_up()
vehicle_object.drive()

vehicle_object1= Vehicle('Subaru', 'Forester', 'Crossover')
Vehicle.our_class()
print(vehicle_object1.brand)
print(vehicle_object1.model)
print(vehicle_object1.type)
vehicle_object.fuel_up()
vehicle_object1.drive()

vehicle_object2= Vehicle('Ford', 'Explorer', 'SUV')
Vehicle.our_class()
print(vehicle_object2.brand)
print(vehicle_object2.model)
print(vehicle_object2.type)
vehicle_object2.fuel_up()
vehicle_object2.drive()


"""
Iterator and for loop
a=("hello")
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
for i in a:
    if i=="o":
        break
    print(i)
"""