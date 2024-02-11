#!/usr/bin/env python3
from brain_games.games.prime import get_num_and_prime_ans
from brain_games.engine import play_game
from brain_games.consts import PRIME_INSTRUCTION


def main():
    '''Запуск prime'''
    play_game(get_num_and_prime_ans, PRIME_INSTRUCTION)


if __name__ == '__main__':
    main()
