"""
Alfred Gachanja
29-08-2023
In this program I am learning how to test classes.
"""

class AnonymousSurvey():
    #Collects anonymous answers to a survey question.

    def __init__(self, question):
        #Store question and prepare to store response.
        self.question = question
        self.responses = []

    def show_question(self):
        #Show the question.
        print(self.question)

    def store_response(self, new_response):
        #Store a single response to the survey
        self.responses.append(new_response)

    def show_results(self):
        #Show all the responses given.
        print("Survey results: ")
        for response in self.responses:
            print(f'- {response}')