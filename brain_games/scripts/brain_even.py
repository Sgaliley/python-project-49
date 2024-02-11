#!/usr/bin/env python3
from brain_games.games.even import get_num_and_even_ans
from brain_games.engine import play_game
from brain_games.consts import EVEN_INSTRUCTION


def main():
    '''Запуск even'''
    play_game(get_num_and_even_ans, EVEN_INSTRUCTION)


if __name__ == '__main__':
    main()
