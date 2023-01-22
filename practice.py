# from functions import get_water_state
#
#
# temperature = float(input('Enter water temperature: '))
# print(get_water_state(temperature))

from random import randint

lowerBound = int(input('Enter the lower bound: '))
upperBound = int(input('Enter the upper bound: '))

print(randint(lowerBound, upperBound))