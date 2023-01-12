import os
import gspread
from google.oauth2.service_account import Credentials

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
"""
print("\nPlease answer the following questions by choosing one of the provided answers.\n")
q_list = [
        ["question 1", "Do you commute most often by ", "car", "bicycle", "public transport", "other", ],
        ["question 2", "Where do you most often learn about climate change ", "internet", "radio/tv", "newspaper", "other", ],
        ["question 3", "Which of the following do you think affects you the most ", "air pollution", "water pollution", "soil pollution", "other", ],
        ["question 4", "What is your age ", "under 18", "19-30", "31-49", "50+", ]
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
        if answer == "car" or answer == "bicycle" or answer == "public transport" or answer == "other" or answer == "internet" or answer == "radio/tv" or answer == "newspaper" or answer == "air pollution" or answer == "water pollution" or answer == "soil pollution" or answer == "under 18" or answer == "19-30" or answer == "31-49" or answer == "50+":
            answers_list.append(answer)
            break
        else:
            print(f"You must choose one answer from the list above. You provided:\n" f"{(answer)}\n")
            answer = input("Please type your answer here: \n")
            print("")

print('Thank you for completing the survey')
"""
Add all answers from the answers list to the google worksheet
"""

worksheet_to_update = SHEET.worksheet('count')
# add to the worksheet
worksheet_to_update.append_row(answers_list)
