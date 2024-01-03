from brain_games.cli import welcome_user, answer_string
import random
import operator
import math


def num_random1():
    num = random.randint(1, 10)
    return num

def num_random2():
    num = random.randint(11, 100)
    return num


def brain_even():
    name = welcome_user()
    count = 3
    while count:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        num = num_random1()
        print(f'Question: {num}')
        answer = answer_string()
        count -= 1
        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(.', end=' ')
            if answer == 'no':
                print('Correct answer was "yes".')
            elif answer == 'yes':
                print('Correct answer was "no".')
            else:
                print('Correct answer was "yes", "no".')
            print(f'Let\'s try again, {name}!')
            quit()
    print(f'Congratulations, {name}!')


def brain_calc():
    name = welcome_user()
    count = 3
    while count:
        print('What is the result of the expression?')
        ops = {'+':operator.add, '-':operator.sub, '*':operator.mul}
        num_rand1 = num_random1()
        num_rand2 = num_random1()
        op = random.choice(list(ops.keys()))
        response = ops.get(op)(num_rand1,num_rand2)
        print(f'Question: {num_rand1} {op} {num_rand2}')
        answer = int(answer_string())
        count -= 1
        if response == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{response}".')
            print(f'Let\'s try again, {name}!')
            quit()
    print(f'Congratulations, {name}!')


def brain_gcd():
    name = welcome_user()
    count = 3
    while count:
        print('What number is missing in the progression?')
        num_rand1 = num_random1()
        num_rand2 = num_random1()
        response = math.gcd(num_rand1, num_rand2)
        print(f'Question: {num_rand1} {num_rand2}')
        answer = int(answer_string())
        count -= 1
        if response == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{response}".')
            print(f'Let\'s try again, {name}!')
            quit()
    print(f'Congratulations, {name}!')


def brain_progression():
    name = welcome_user()
    count = 3
    while count:
        print('What is the result of the expression?')
        num_rand1 = num_random1()
        num_rand2 = num_random2()
        num_rand3 = num_random1()
        lst = [i for i in range(num_rand1, num_rand2, num_rand1)]
        num = random.randint(0, len(lst)-1)
        response = lst[num]
        lst[num] = '..'
        print(f'Question: {" ".join(str(i) for i in lst)}')
        answer = int(answer_string())
        count -= 1
        if response == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{response}".')
            print(f'Let\'s try again, {name}!')
            quit()
    print(f'Congratulations, {name}!')
