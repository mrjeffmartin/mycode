#!/usr/bin/env python3
message1 = 'Sustained winds of '
message2 = ' MPH would be considered a category '
print('What is the hurricane wind speed? ')
windspeed = float(input())
if windspeed >= 157:
    category = '5.'
elif windspeed >= 130:
    category = '4.'
elif windspeed >= 111:
    category = '3.'
elif windspeed >= 96:
    category = '4.'
elif windspeed >= 74:
    category = '3.'
elif windspeed < 74:
    category = '0'

if category is '0':
    print('Winds with a speed of ' + str(windspeed) + ' is not considered a hurricane.') 
else:
    print(message1 + str(windspeed) + message2 + category)
