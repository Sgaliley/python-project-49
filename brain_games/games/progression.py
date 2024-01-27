from random import randint

def game():
    '''Прогрессия. Поиск пропущенных чисел в последовательности чисел'''
    print('What number is missing in the progression?')
    num = randint(1, 10)
    step = randint(1, 10)
    length = randint(5, 10)
    lst = [str(num + i * step) for i in range(length)]
    rand_num = randint(0, len(lst) - 1)
    game_answer = lst[rand_num]
    lst[rand_num] = '..'
    print(f'Question: {" ".join(lst)}')
    return game_answer
