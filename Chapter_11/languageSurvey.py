"""
Alfred Gachanja
29-08-2023
This program uses the class module for a language survey.
"""

from survey import AnonymousSurvey

#Define a question and make a survey.
question = "What language did you first learn to speak."
my_survey = AnonymousSurvey(question)

#Show the question and store the responses.
my_survey.show_question()
while True:
    responses = input("Language: ")
    if responses == 'q':
        break
    my_survey.store_response(responses)

#Show the survey results.
print("\nThank you every one who participated in the survey.")
my_survey.show_results()
    