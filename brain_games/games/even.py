import random
from brain_games.engine import play_game
from brain_games.consts import EVEN_INSTRUCTION, MIN_NUM, MAX_NUM


def is_even(num):
    return num % 2 == 0


def get_num_and_even_ans():
    '''Определение четного числа'''
    num = random.randint(MIN_NUM, MAX_NUM)
    game_answer = 'yes' if is_even(num) else 'no'
    return num, game_answer


def run_even_game():
    play_game(get_num_and_even_ans, EVEN_INSTRUCTION)
