#!/usr/bin/env python3
from brain_games.cli import welcome_user, answer_string
from brain_games.logic import num_random
import math 


def main():
    name = welcome_user()
    count = 3
    while count:
        print('What is the result of the expression?')
        num_random1 = num_random()
        num_random2 = num_random()
        response = math.gcd(num_random1, num_random2)
        print(f'Question: {num_random1} {num_random2}')
        print(response)
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
