'''friends_favor_flowers = dict({'Alex': 'field flowers',
                              'Kate': 'daffodil',
                              'Eva': 'artichoke flower',
                              'Daniel': 'tulip'})
print(friends_favor_flowers)'''

# word = input()
# print(f'{word} has {len(word)} letters')
'''income = int(input())
percent = 0
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
else:
    percent = 28
calculated_tax = '%.0f' % (income * percent / 100)
print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')'''

# nickname = input()
# profession = input()
# print(f'http://example.com/{nickname}/desirable/{profession}/profile')
# print('http://example.com/{}/desirable/{}/profile'.format(nickname, profession))

# number = float(input())
# count = int(input())
# print('{:.{precision}f}'.format(number, precision=count))
# print('{:.{}f}'.format(number, count))
# print(f'{number:.{count}f}')

# movie, director, year = input(), input(), input()
# print(f'{movie} (dir. {director}) came out in {year}')
# print(f'{input()} (dir. {input()}) came out in {input()}')
# print('{0} (dir. {1}) came out in {2}'.format(input(), input(), input()))

# from random import choice
# from math import copysign
# import random
# import string

# print(digits)
# num = random.random()
# print('%.5f' % num)
# print(f'{random.random():.8f}')
# print(choice(['red', 'green', 'yellow']))

# input_string = input()
# print(string.capwords(input_string, sep=None))

# x, y = map(float, input().split(' '))
# print(type(x)) # type <class 'float'>
# print(copysign(x, y))


'''import tic_tac_toe
tic_tac_toe.main()'''

import bank
bank.menu_account()
