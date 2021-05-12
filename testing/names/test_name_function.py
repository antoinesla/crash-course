import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''tests for "name_function.py"'''

    def test_first_last_name(self):
        '''do names like "janis joplin" work?'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        '''do names like "billy bob thornton" work?'''
        formatted_name = get_formatted_name('billy', 'thornton', 'bob')
        self.assertEqual(formatted_name, 'Billy Bob Thornton ')

if __name__ == '__main__':
    unittest.main()