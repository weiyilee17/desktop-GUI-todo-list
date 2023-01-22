"""

import glob

txtFiles = glob.glob('./*.txt')

for filePath in txtFiles:
    with open(filePath, 'r') as file:
        print(file.read())

import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))
    print(data)

city = input('Enter a city: ')

for [station, temperature] in data[1:]:
    if station == city:
        print(temperature)

# shell util
import shutil

shutil.make_archive('output', 'zip', './')

import webbrowser

userQuery = input('Enter a search term: ').replace(' ', '+')

webbrowser.open(f'https://www.google.com/search?q={userQuery}')

"""

import json


with open('questions.json', 'r') as file:
    content = file.read()
    data = json.loads(content)

    for singleQuestion in data:
        print(singleQuestion['questionText'])

        for index, singleOption in enumerate(singleQuestion['options']):
            print(index + 1, ':', singleOption)

        userChoice = int(input('Enter your choice: '))

        singleQuestion['userChoice'] = userChoice

    print('')
    score = 0

    for index, singleQuestion in enumerate(data):

        result = ''

        if singleQuestion['userChoice'] == singleQuestion['correctAnswer']:
            score += 1
            result = 'Correct Answer'
        else:
            result = 'Wrong Answer'

        print(f'{index + 1}. {result}. Your answer: {singleQuestion["userChoice"]}, '
              f'the correct answer is: {singleQuestion["correctAnswer"]}')

    print(f'Score: {score} / {len(data)}')