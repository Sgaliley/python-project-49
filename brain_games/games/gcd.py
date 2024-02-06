import random
import math
from brain_games.engine import play_game
from brain_games.consts import GCD_INSTRUCTION, MIN_NUM, MAX_NUM


def get_nums_pair_and_gcd():
    '''Определение наибольшего общего делителя(НОД)'''
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    game_answer = str(math.gcd(num1, num2))
    num = f'{num1} {num2}'
    return num, game_answer


def run_gcd_game():
    play_game(get_nums_pair_and_gcd, GCD_INSTRUCTION)
