class Restaurant:
    """tutorial class to model restaurant"""

    def __init__(self, name, cuisine):
        """initialises restaurant name and type of cuisine"""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.numbers_served = 0

    def describe_restaurant(self):
        """describes restaurant with welcoming message"""
        print(f'welcome to {self.restaurant_name}',\
              f'where we serve {self.cuisine_type}')
    
    def open_restaurant(self):
        """prints message to announce restaurant is open"""
        print(f'{self.restaurant_name} is now open')

    def set_number_served(self, clients):
        """sets the number of clients served by restaurant"""
        self.numbers_served = clients
    
    def increment_number_served(self, clients):
        """increments the number of clients served by restaurant"""
        if clients < 0:
            print("can't increment by a negative number")
        else:
            self.numbers_served += clients

    def reset_number_served(self):
        """resets the number of clients served to 0"""
        self.numbers_served = 0

    def display_number_served(self):
        """prints the number of clients served by restaurant"""
        print(f"numbers of clients served: {self.numbers_served}")

class IceCreamStand(Restaurant):
    '''tutorial class to model ice cram stand based on restaurant class'''

    def __init__(self, name, flavors_served):
        '''
        initializes restaurant attributes and specific ones for ice cream stand
        '''
        super().__init__(name, 'ice cream')
        self.flavors_served = flavors_served

    def describe_flavors_served(self):
        '''lists flavors served by ice cream stand'''
        print('here are the flavors that we serve:')
        for flavor in self.flavors_served:
            print(f'\t{flavor}')