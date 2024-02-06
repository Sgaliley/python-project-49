from brain_games.cli import welcome_user, answer_string
from brain_games.consts import AMOUNT_OF_ROUNDS


def play_game(get_question_and_answer, instruction):
    name = welcome_user()
    print(f'{instruction}')
    for _ in range(AMOUNT_OF_ROUNDS):
        num, game_answer = get_question_and_answer()
        print(f'Question: {num}')
        user_answer = answer_string()
        if game_answer == user_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{game_answer}".')
            print(f'Let\'s try again, {name}!')
            quit()
    print(f'Congratulations, {name}!')
