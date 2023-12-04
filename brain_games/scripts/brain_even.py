#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    count = 3
    while count:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        num_random = random.randint(1, 99)
        print(f'Question: {num_random}')
        answer = prompt.string('Your answer: ')
        count -= 1
        if num_random % 2 == 0 and answer == 'yes' or num_random % 2 != 0 and answer == 'no':
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


if __name__ == '__main__':
    main()
