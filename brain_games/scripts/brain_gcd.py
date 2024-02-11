#!/usr/bin/env python3
from brain_games.games.gcd import get_nums_pair_and_gcd
from brain_games.engine import play_game
from brain_games.consts import GCD_INSTRUCTION


def main():
    '''Запуск gcd'''
    play_game(get_nums_pair_and_gcd, GCD_INSTRUCTION)


if __name__ == '__main__':
    main()
