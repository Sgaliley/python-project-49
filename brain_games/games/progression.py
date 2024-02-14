import random
from brain_games.consts import (
    MIN_PROGRESSION_LENGTH,
    MAX_PROGRESSION_LENGTH,
    MIN_NUM,
    MAX_NUM,
)


def progression_calc(num, step, length):
    return [num + i * step for i in range(length)]


def miss_num(progression, rand_num):
    prog_copy = progression.copy()
    prog_copy[rand_num] = '..'
    return prog_copy


def get_progression_and_miss_num():
    '''Прогрессия. Поиск пропущенных чисел в последовательности чисел'''
    num = random.randint(MIN_NUM, MAX_NUM)
    step = random.randint(MIN_NUM, MAX_NUM)
    length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    progression = progression_calc(num, step, length)
    rand_num = random.randint(0, length - 1)
    game_answer = str(progression[rand_num])
    prog_with_missed_num = miss_num(progression, rand_num)
    return " ".join(map(str, prog_with_missed_num)), game_answer
