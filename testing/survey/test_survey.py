import unittest
from survey import AnonymousSurvey

class TesAnonymousSurvey(unittest.TestCase):
    '''tests for the class AnonymousSurvey'''

    def setUp(self):
        '''create a survey and a set of responses for use in all methods'''
        question = 'what language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'chinese', 'french']

    def test_store_single_response(self):
        '''test that a single response is stored properly'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        '''test that three responses are stored properly'''

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)




if __name__ == '__main__':
    unittest.main()