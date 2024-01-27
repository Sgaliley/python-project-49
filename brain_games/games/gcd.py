from random import randint
import math


def game():
    '''Определение наибольшего общего делителя(НОД)'''
    print('Find the greatest common divisor of given numbers.')
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    game_answer = str(math.gcd(num1, num2))
    print(f'Question: {num1} {num2}')
    return game_answer
