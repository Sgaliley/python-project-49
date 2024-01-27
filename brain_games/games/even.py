from random import randint


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game():
    '''Определение четного числа'''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num = randint(1, 100)
    print(f'Question: {num}')
    game_answer = is_even(num)
    return game_answer
