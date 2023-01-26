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

import json

with open('questions.json', 'r') as file:
    content = file.read()
    print(content)
