class Employee:
    '''practice class simulating an employee record'''

    def __init__(self, first_name, last_name, annual_salary, middle_name=''):
        '''inits first and last name and salary, and middle name if any'''
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        if middle_name: self.middle_name = middle_name

    def give_raise(self, raise_amount=5000):
        '''raises employee salary, default amount is 5000'''
        self.annual_salary += raise_amount
    
    def get_salary(self):
        '''returns annual salary of employee'''
        return self.annual_salary