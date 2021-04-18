from car import Car

class Battery:
    def __init__(self, capacity):
        '''initializes attributes for battery'''
        self.capacity = capacity
    
    def get_battery_capacity(self):
        '''returns capacity of battery'''
        return self.capacity

    def set_battery_capacity(self, new_capacity):
        '''sets capacity of the battery'''
        self.capacity = new_capacity

    def describe_battery(self):
        '''prints capacity of current battery'''
        print(f'this battery has a {self.capacity}-kWH capacity.')


class ElectricCar(Car):
    """Simple model of electric car based on model of car"""

    def __init__(self, make, model, year, battery_capacity):
        '''
        initializes attributes similar to parent class
        plus attributes specific to electric car
        '''
        super().__init__(make, model, year)
        self.battery = Battery(battery_capacity)

    def fill_gas_tank(self):
        '''overrides method as electric cars don't have tank'''
        print("you can't fill up the tank of an electric car!")

    def decribe_car_battery(self):
        '''prints capacity of battery attached to car'''
        print(f'this car has battery of',
              f'{self.battery.get_battery_capacity()}-kWH')

    def upgrade_battery(self):
        '''upgrade car battery to 100kWH if it is 75kWH'''
        if self.battery.get_battery_capacity() == 75:
            print('upgrading battery capacity')
            self.battery.set_battery_capacity(100)
        elif self.battery.get_battery_capacity == 100:
            print('battery is already at maximum capacity')

    def describe_range(self):
        '''print max range of car based on battery capacity'''
        if self.battery.get_battery_capacity() == 75: range = 200
        elif self.battery.get_battery_capacity() == 100: range = 300
        print(f'this car can go {range} miles on a full charge')
