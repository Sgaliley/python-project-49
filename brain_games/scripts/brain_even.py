#!/usr/bin/env python3
from brain_games.cli import welcome_user, answer_string
from brain_games.logic import num_random


def main():
    name = welcome_user()
    count = 3
    while count:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        num = num_random()
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


if __name__ == '__main__':
    main()
