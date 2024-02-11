import random
from brain_games.consts import (
    MIN_PROGRESSION_LENGTH,
    MAX_PROGRESSION_LENGTH,
    MIN_NUM,
    MAX_NUM,
)


def progression_calc(num, step, length):
    return [str(num + i * step) for i in range(length)]


def progresion_to_str_and_miss_num(length, lst):
    lst_copy = lst.copy()
    rand_num = random.randint(0, length - 1)
    game_answer = lst_copy[rand_num]
    lst_copy[rand_num] = '..'
    prog_with_missed_num = " ".join(lst_copy)
    return game_answer, prog_with_missed_num


def get_progression_and_miss_num():
    '''Прогрессия. Поиск пропущенных чисел в последовательности чисел'''
    num = random.randint(MIN_NUM, MAX_NUM)
    step = random.randint(MIN_NUM, MAX_NUM)
    length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    lst = progression_calc(num, step, length)
    game_answer, prog_with_missed_num = progresion_to_str_and_miss_num(
        length,
        lst,
    )
    return prog_with_missed_num, game_answer
