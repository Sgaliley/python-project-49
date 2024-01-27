from random import randint
import math


def is_prime(num):
    if num < 2:
        return 'no'
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def game():
    '''Определение простого числа'''
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num = randint(1, 100)
    print(f'Question: {num}')
    game_answer = is_prime(num)
    return game_answer
