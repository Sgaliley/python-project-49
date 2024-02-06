import operator
import random
from brain_games.engine import play_game
from brain_games.consts import CALC_INSTRUCTION, MIN_NUM, MAX_NUM


def get_math_expression_and_result():
    '''Калькулятор. Арифметические выражения, которые необходимо вычислить'''
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    op = random.choice(list(ops.keys()))
    game_answer = str(ops.get(op)(num1, num2))
    expression = f'{num1} {op} {num2}'
    return expression, game_answer


def run_calc_game():
    play_game(get_math_expression_and_result, CALC_INSTRUCTION)
