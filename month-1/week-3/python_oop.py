class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def describe(self):
    return f"This is a {self.make} {self.model}"

class Car(Vehicle):
  def __init__(self, make, model, num_doors):
    super().__init__(make, model)
    self.__num_doors = num_doors
  def describe(self):
    return f"This is a {self.make} {self.model} and has {self.__num_doors} doors"
  def get_num_doors(self):
    return self.__num_doors
  
class Bike(Vehicle):
  def __init__(self, make, model, bike_type):
    super().__init__(make, model)
    self.bike_type = bike_type
  def describe(self):
    return f"This is a {self.make} {self.model} of type {self.bike_type}"
  
vehicles = [
  Car("Toyota", "Camry", 4),
  Bike("Honda", "CBR500R", "Sport"),
  Vehicle("Ford", "Mustang")
]

for vehicle in vehicles:
  print(vehicle.describe())
