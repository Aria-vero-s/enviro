import os
import gspread
from google.oauth2.service_account import Credentials
from collections import Counter


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Enviro')

"""
Survey starts here. The questions are in a group list.
I used https://realpython.com/python-quiz-application/ to help me understand how to build this survey.
"""
print("\nPlease answer the following questions by choosing one of the provided answers.\n")
q_list = [
        ["question 1", "Do you commute most often by ", "a: car", "b: bicycle", "c: public transport", "d: other", ],
        ["question 2", "Where do you most often learn about climate change ", "a: internet", "b: radio/tv", "c: newspaper", "d: other", ],
        ["question 3", "Which of the following do you think affects you the most ", "a: air pollution", "b: water pollution", "c: soil pollution", "d: other", ],
        ["question 4", "What is your age ", "a: under 18", "b: 19-30", "c: 31-49", "d: 50+", ]
            ]
"""
Get answer input from the user.
Run a while loop to collect a valid string of answers from the user via the terminal.
The loop will repeatedly request an answer until it is valid.
"""

# save list of answers
answers_list = []

for q in q_list[0:5]:
    answer = input(f"{q[1]}:\n - {q[2]} \n - {q[3]} \n - {q[4]} \n - {q[5]} \nplease type your answer here: \n")
    print("")
    while True:
        if answer == "a" or answer == "b" or answer == "c" or answer == "d":
            answers_list.append(answer)
            break
        else:
            print(f"You must choose one answer from the list above. You provided:\n" f"{(answer)}\n")
            answer = input("Please type your answer here: \n")
            print("")

print('Thank you for completing the survey \n')
"""
Add all answers from the answers list to the google worksheet
"""

worksheet_to_update = SHEET.worksheet('count')
# add to the worksheet
worksheet_to_update.append_row(answers_list)

x = SHEET.worksheet('count').col_values(1)
print('These were the most popular answers out of the', len(x)-8, 'participants: \n')

"""
I used the https://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list to help me build the next section.
And https://www.geeksforgeeks.org/python-string-join-method/ to clean up the answers
"""

q_1_answers = SHEET.worksheet('count').col_values(5)
col_1 = (SHEET.worksheet('count').col_values(1))
most_common_words1 = [col_1 for col_1, word_count in Counter(col_1).most_common(1)]

print(max(q_1_answers), 'participants answered:')
if most_common_words1 == ['a']:
    print('car, for question 1')
elif pop_answer1_no_brackets == ['b']:
    print('bicycle, for question 1')
elif pop_answer1_no_brackets == ['c']:
    print('public transport, for question 1')
elif pop_answer1_no_brackets == ['d']:
    print('other, for question 1')
else: print('invalid')

q_2_answers = SHEET.worksheet('count').col_values(6)
col_2 = Counter(SHEET.worksheet('count').col_values(2))
most_common_words2 = [col_2 for col_2, word_count in Counter(col_2).most_common(1)]

pop_answer2_no_brackets = ""
pop_answer2_no_brackets = pop_answer2_no_brackets.join(most_common_words2)

print(max(q_2_answers), 'participants answered:')
if pop_answer2_no_brackets == 'a':
    print('internet, for question 2')
elif pop_answer2_no_brackets == 'b':
    print('radio/tv, for question 2')
elif pop_answer2_no_brackets == 'c':
    print('newspaper, for question 2')
elif pop_answer2_no_brackets == 'd':
    print('other, for question 2')
else: print('invalid')

q_3_answers = SHEET.worksheet('count').col_values(7)
col_3 = Counter(SHEET.worksheet('count').col_values(3))
most_common_words3 = [col_3 for col_3, word_count in Counter(col_3).most_common(1)]

pop_answer3_no_brackets = ""
pop_answer3_no_brackets = pop_answer3_no_brackets.join(most_common_words3)

print(max(q_3_answers), 'participants answered:')
if pop_answer3_no_brackets == 'a':
    print('air pollution, for question 3')
elif pop_answer3_no_brackets == 'b':
    print('water pollution, for question 3')
elif pop_answer3_no_brackets == 'c':
    print('soil pollution, for question 3')
elif pop_answer3_no_brackets == 'd':
    print('other, for question 3')
else: print('invalid')

q_4_answers = SHEET.worksheet('count').col_values(8)
col_4 = Counter(SHEET.worksheet('count').col_values(4))
most_common_words4 = [col_4 for col_4, word_count in Counter(col_4).most_common(1)]

pop_answer4_no_brackets = ""
pop_answer4_no_brackets = pop_answer4_no_brackets.join(most_common_words4)

print(max(q_4_answers), 'participants answered:')
if pop_answer4_no_brackets == 'a':
    print('under 18, for question 4')
elif pop_answer4_no_brackets == 'b':
    print('19-30, for question 4')
elif pop_answer4_no_brackets == 'c':
    print('31-49, for question 4')
elif pop_answer4_no_brackets == 'd':
    print('50+, for question 4')
else: print('invalid')
