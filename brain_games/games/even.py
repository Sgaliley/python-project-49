import random
from brain_games.consts import MIN_NUM, MAX_NUM


def is_even(num):
    return num % 2 == 0


def get_num_and_even_ans():
    '''Определение четного числа'''
    num = random.randint(MIN_NUM, MAX_NUM)
    game_answer = 'yes' if is_even(num) else 'no'
    return num, game_answer
