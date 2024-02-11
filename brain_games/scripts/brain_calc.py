#!/usr/bin/env python3
from brain_games.games.calc import get_math_expression_and_result
from brain_games.engine import play_game
from brain_games.consts import CALC_INSTRUCTION


def main():
    '''Запуск calc'''
    play_game(get_math_expression_and_result, CALC_INSTRUCTION)


if __name__ == '__main__':
    main()
