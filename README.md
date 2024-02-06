### Hexlet tests and linter status:
[![Actions Status](https://github.com/Sgaliley/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Sgaliley/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b9a35673e6737e98d91c/maintainability)](https://codeclimate.com/github/Sgaliley/python-project-49/maintainability)



## Описание
«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново.  

Игры:
* Определение четного числа
* Калькулятор. Арифметические выражения, которые необходимо вычислить
* Определение наибольшего общего делителя
* Прогрессия. Поиск пропущенных чисел в последовательности чисел
* Определение простого числа

Пример игры:
```
brain-progression
Welcome to the Brain Game!
What number is missing in this progression?
May I have your name? Roman
Hello, Roman!
Question: 14 .. 18 20 22 24 26 28
Your answer: 16 # Пользователь вводит ответ
Correct!
Question: 5 6 7 8 9 .. 11 12
Your answer: 10 # Пользователь вводит ответ
Correct!
Question: 12 15 18 21 .. 27 30 33
Your answer: 24 # Пользователь вводит ответ
Correct!
Congratulations, Roman!
```

## Установка

Перед установкой пакета необходимо убедиться, что у вас установлен Python версии 3.11 или выше:
```bash
# Linux:
>> python3 --version # or python -V
Python 3.11.0+
```
обновить
```
>> sudo apt-get update && sudo apt-get upgrade python3.X
```
установить
```
>> sudo apt update && sudo apt-get install python3.X
```
Установить PIP и Poetry и make

```
>> sudo apt-get install python3-pip
>> sudo apt-get install python3-poetry
>> sudo apt-get install make
```

Клонируем проект
```
# clone via HTTPS:
>> git clone https://github.com/Sgaliley/python-project-49.git
```
Переходим в проект и устанавливаем пакет
```
>> cd python-project-lvl1
>> make build
>> make package-install

```
Запуск игр
```
>> brain-even
>> brain-calc
>> brain-gcd
>> brain-progression
>> brain-prime
```


### Демонстрация Brain-even (Определение четного числа)

[![asciicast](https://asciinema.org/a/ADL8L8ZInFhv1W2FW0TzAQlO4.svg)](https://asciinema.org/a/ADL8L8ZInFhv1W2FW0TzAQlO4)

### Демонстрация Brain-calc (Калькулятор. Арифметические выражения, которые необходимо вычислить)

[![asciicast](https://asciinema.org/a/gAfTVQxavyI5J3BGyUwxVH8LH.svg)](https://asciinema.org/a/gAfTVQxavyI5J3BGyUwxVH8LH)

### Демонстрация Brain-gcd (Определение наибольшего общего делителя)

[![asciicast](https://asciinema.org/a/Jj5aotUf8fj00LMLfMmmPCPPj.svg)](https://asciinema.org/a/Jj5aotUf8fj00LMLfMmmPCPPj)

### Демонстрация Brain-progression (Прогрессия. Поиск пропущенных чисел в последовательности чисел)

[![asciicast](https://asciinema.org/a/M1oDATXMyEA12s81gHyom2icy.svg)](https://asciinema.org/a/M1oDATXMyEA12s81gHyom2icy)

### Демонстрация Brain-prime (Определение простого числа  )

[![asciicast](https://asciinema.org/a/IclxuyUtuckfzWXXJlOuj7kIu.svg)](https://asciinema.org/a/IclxuyUtuckfzWXXJlOuj7kIu)