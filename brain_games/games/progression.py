import random
from brain_games.engine import play_game
from brain_games.consts import (
    MIN_PROGRESSION_LENGTH,
    MAX_PROGRESSION_LENGTH,
    PROGRESSION_INSTRUCTION,
    MIN_NUM,
    MAX_NUM,
)


def get_progression_and_miss_num():
    '''Прогрессия. Поиск пропущенных чисел в последовательности чисел'''
    num = random.randint(MIN_NUM, MAX_NUM)
    step = random.randint(MIN_NUM, MAX_NUM)
    length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    lst = [str(num + i * step) for i in range(length)]
    rand_num = random.randint(0, length - 1)
    game_answer = lst[rand_num]
    lst[rand_num] = '..'
    prog_with_missed_num = " ".join(lst)
    return prog_with_missed_num, game_answer


def run_progression_game():
    play_game(get_progression_and_miss_num, PROGRESSION_INSTRUCTION)
