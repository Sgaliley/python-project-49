#!/usr/bin/env python3
from brain_games.games.progression import get_progression_and_miss_num
from brain_games.engine import play_game
from brain_games.consts import PROGRESSION_INSTRUCTION


def main():
    '''Запуск progression'''
    play_game(get_progression_and_miss_num, PROGRESSION_INSTRUCTION)


if __name__ == '__main__':
    main()
