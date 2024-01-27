from brain_games.cli import welcome_user, answer_string


def play_game(game):
    name = welcome_user()
    for _ in range(3):
        game_answer = game()
        user_answer = answer_string()
        if game_answer == user_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{game_answer}".')
            print(f'Let\'s try again, {name}!')
            quit()
    print(f'Congratulations, {name}!')
