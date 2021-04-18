from car import Car
from electric_car import ElectricCar

clio = Car('Renault', 'Clio', '2015')
print(clio.get_descriptive_name())
clio.fill_gas_tank()

tesla = ElectricCar("Tesla", "Model X", "2018", 75)
print(tesla.get_descriptive_name())
# tesla.fill_gas_tank()
tesla.decribe_car_battery()
tesla.describe_range()
tesla.upgrade_battery()
tesla.decribe_car_battery()
tesla.describe_range()

# when you create a child class, the parent class must be part of the current 
# and must appear before the child class in the file