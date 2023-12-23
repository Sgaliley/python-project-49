#!/usr/bin/env python3
from brain_games.cli import welcome_user, answer_string
from brain_games.logic import num_random
import random
import operator


def main():
    name = welcome_user()
    count = 3
    while count:
        print('What is the result of the expression?')
        ops = {'+':operator.add, '-':operator.sub, '*':operator.mul}
        num_random1 = num_random()
        num_random2 = num_random()
        op = random.choice(list(ops.keys()))
        response = ops.get(op)(num_random1,num_random2)
        print(f'Question: {num_random1} {op} {num_random2}')
        answer = int(answer_string())
        count -= 1
        if response == answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{response}".')
            print(f'Let\'s try again, {name}!')
            quit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
