"""
Alfred Gachanja
31-08-2023
In this program I am testing the AnonymousSurvey in survey.py
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    #Tests the class AnonymousSurvey

    def setUp(self):
        #Creating a survey and a set of responses for use in all test methods.
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Swahili', 'Japanese']

    def test_store_single_response(self):
        #Tests that single response is stored well.
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        #Tests that three individual responses are stored correctly.

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()