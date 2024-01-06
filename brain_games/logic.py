from brain_games.cli import welcome_user, answer_string
import random
import operator
import math


def num_random(range_start, range_end):
    return random.randint(range_start, range_end)


def check_answer(game_answer, user_answer, name):
    if game_answer == user_answer:
        print('Correct!')
    else:
        print(f'"{user_answer}" is wrong answer ;(. '
              f'Correct answer was "{game_answer}".')
        print(f'Let\'s try again, {name}!')
        quit()


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def is_prime(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k = k + 1
    if (k <= 0):
        return 'yes'
    else:
        return 'no'


def brain_even():
    '''Определение четного числа'''
    name = welcome_user()
    for _ in range(3):
        print('Answer "yes" if the number is even, otherwise answer "no".')
        num = num_random(1, 100)
        print(f'Question: {num}')
        game_answer = is_even(num)
        user_answer = answer_string()
        check_answer(game_answer, user_answer, name)
    print(f'Congratulations, {name}!')


def brain_calc():
    '''Калькулятор. Арифметические выражения, которые необходимо вычислить'''
    name = welcome_user()
    for _ in range(3):
        print('What is the result of the expression?')
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        num1 = num_random(1, 20)
        num2 = num_random(1, 20)
        op = random.choice(list(ops.keys()))
        game_answer = ops.get(op)(num1, num2)
        print(f'Question: {num1} {op} {num2}')
        user_answer = int(answer_string())
        check_answer(game_answer, user_answer, name)
    print(f'Congratulations, {name}!')


def brain_gcd():
    '''Определение наибольшего общего делителя(НОД)'''
    name = welcome_user()
    for _ in range(3):
        print('Find the greatest common divisor of given numbers.')
        num1 = num_random(1, 20)
        num2 = num_random(1, 20)
        game_answer = math.gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        user_answer = int(answer_string())
        check_answer(game_answer, user_answer, name)
    print(f'Congratulations, {name}!')


def brain_progression():
    '''Прогрессия. Поиск пропущенных чисел в последовательности чисел'''
    name = welcome_user()
    for _ in range(3):
        print('What number is missing in the progression?')
        num1 = num_random(1, 10)
        step = num_random(1, 10)
        length = num_random(5, 10)
        lst = [str(num1 + i * step) for i in range(length)]
        num = random.randint(0, len(lst) - 1)
        game_answer = lst[num]
        lst[num] = '..'
        print(f'Question: {" ".join(lst)}')
        user_answer = answer_string()
        check_answer(game_answer, user_answer, name)
    print(f'Congratulations, {name}!')


def brain_prime():
    '''Определение простого числа'''
    name = welcome_user()
    for _ in range(3):
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        num = num_random(1, 100)
        print(f'Question: {num}')
        game_answer = is_prime(num)
        user_answer = answer_string()
        check_answer(game_answer, user_answer, name)
    print(f'Congratulations, {name}!')
