# Enviro

Enviro is a Python terminal survey, which runs the Code Institute mock terminal on Heroku.

The user will answer four questions on the topic of climate change. After completion, the answers are automatically compiled in a separate google sheet document.

Here is the live version of my project:

https://enviro-heroku.herokuapp.com/

Here is the google sheet:

https://docs.google.com/spreadsheets/d/1Rcz8dzrTXvPHjxwoMHBXs2aZOEnhtcarwN_9A1e86hA/edit?usp=sharing

<img src="images/multi-device-mockup.png">


# How to complete the survey

After clicking on 'run program', the user is prompted with the following statement: 'Please answer the following questions by choosing one of the provided answers.' The program then shows a question with a list of 4 answers to choose from. The user simply needs to type the answer from the list and press enter and repeat for all 4 questions.


<img src="images/question1.png" width="600">


After completing the survey, the answers are sent to the linked google sheet where they are compiled automatically for the survey analyst. In the google sheet, the survey analyst can examine the count for each answer and see which ones are the most frequent.


<img src="images/googlesheet-green.png" width="600">


# Features

## Existing features

- The questions are displayed one at a time in order
- The multiple answers are grouped under their respective questions
- Accepts user inputs
- Input validation and error-checking
    - The answer must be one of the multiple answers provided
    - The answer must be entered in letters only
    - The survey will return the user's wrong input

    <img src="images/wrong-input.png" width="400">
    
- Data sent to linked google sheet
- The quantity of participants is displayed after completion of the survey
- The most popular answers are displayed at the end

<img src="images/popular-answers.png" width="600">

## Future features

- Ability for the participant to go back and change their answer

# Data Model

I decided to use a python list to hold the questions and multiple choice answers. The survey uses a for loop in order to collect the answers and verify if they are entered correctly by the user. The answers are sent to the google sheet using the SHEET variable and google sheet API.

# Testing

I have manually tested this project by doing the following:
- Typed invalid inputs (i.e., numbers and typos) when specific strings are expected
- Tested in my local terminal and the Code Institute Heroku terminal
- No errors were found when passing through the official https://pep8ci.herokuapp.com/

## Bugs

### Solved bugs

- The wrong answers (or user typos) were sent to the google sheet and thus interfered with the exactitude of the answer compilation. The problem was the code 'answers_list.append(answer)' in the else statement. The fix was to simply remove that line of code.

## Bugs remaining

- No bugs remaining.

# Deployment

This project was deployed using Code Institute's mock terminal heroku.

- steps for deployment:
    - Fork or clone this repository
    - Create a new heroku app
    - Set the buildpacks to `Python` and `NodeJS` in that order
    - Link the heroku app to the repository
    - Click on <strong>Deploy</strong>


# Credits

Code Institute for the deployment terminal

https://techsini.com/multi-mockup/index.php for the README.md multi-device mockup image

https://realpython.com/python-quiz-application/ for the tutorial