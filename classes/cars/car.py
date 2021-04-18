class Car:
    """A simple model of a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a neatly formatted string with detailed info"""
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        """Prints a statement showing the car's mileage"""
        print(f"mileage: {self.odometer_reading}")

    def update_odomeger(self, mileage):
        """Updates car's mileage with passed value"""
        if mileage <= self.odometer_reading: 
            print("you can't roll back the odometer")
        else:
            self.odometer_reading = mileage
        
    def incemrent_odometer(self,miles):
        '''increments the odometer of the car by value passed'''
        if miles <= 0:
            print("you can't roll back the odometer")
        else:
            self.odometer_reading += miles

    def fill_gas_tank(self):
        """simulates filling gas tank of the car"""
        print(f'filling the tank of {self.get_descriptive_name()}')