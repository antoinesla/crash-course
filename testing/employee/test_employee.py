import unittest
from employee import Employee

class TestEmployeeRecord(unittest.TestCase):
    '''tests for employee class'''

    def setUp(self):
        '''creates an employee class for use in all methods'''
        first_name = 'john'
        last_name = 'doe'
        salary = 40000
        self.my_employee = Employee(first_name, last_name, salary)

    def test_default_raise(self):
        '''tests raise method with default value (no value passed)'''
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.get_salary(), 45000)
    
    def test_custom_raise(self):
        '''tests raise method with custom value'''
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.get_salary(), 50000)

if __name__ == '__main__':
    unittest.main()