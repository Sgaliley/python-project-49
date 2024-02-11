import random
from brain_games.consts import MIN_NUM, MAX_NUM


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_num_and_prime_ans():
    '''Определение простого числа'''
    num = random.randint(MIN_NUM, MAX_NUM)
    game_answer = 'yes' if is_prime(num) else 'no'
    return num, game_answer
