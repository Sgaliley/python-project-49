import operator
from random import randint, choice


def game():
    '''Калькулятор. Арифметические выражения, которые необходимо вычислить'''
    print('What is the result of the expression?')
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    op = choice(list(ops.keys()))
    game_answer = str(ops.get(op)(num1, num2))
    print(f'Question: {num1} {op} {num2}')
    return game_answer
