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

while True:
    print("Please answer the following questions by choosing one of the provided answers.")

g_list = [
    ["question 1", "Do you commute most often by ", "car", "bicycle", "public transport", "other",],
    ["question 2", "Where do you most often learn about climate change ", "internet", "radio/tv", "newspaper", "other",],
    ["question 3", "Which of the following do you think affect you the most ", "air pollution", "water pollution", "soil pollution", "other",],
    ["question 4", "What is your age ", "under 18", "19-30", "31-49", "50+",]
]

if answer:
    print("Data is valid!")
    break

for q in g_list[0:4]:
    answer = input(f"{q[1]}:\n - {q[2]} \n - {q[3]} \n - {q[4]} \n - {q[5]} \nplease type your answer here: \n")

    if answer == "car" or answer == "bicycle" or answer == "public transport" or answer == "other" or answer == "internet" or answer == "radio/tv" or answer == "newspaper" or answer == "air pollution" or answer == "water pollution" or answer == "soil pollution" or answer == "under 18" or answer == "19-30" or answer == "31-49" or answer == "50+":
        pass
    else:
        raise ValueError(
        f"You must choose one answer from the list above. You provided {(answer)}"
        )
    return False

return True