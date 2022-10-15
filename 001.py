# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint as r
from random import choice as ch


messages = ['Your turn to take sweets', 'take sweets',
            'how many sweets will you take?', "take it, don't be shy", 'your move']


def introduce_players():
    player1 = input("Let's get acquainted. What is your name?\n")
    player2 = 'Candy_bot'
    print(f'I am very pleased, my name is {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('How many candies will we give away?\n '))
    m = int(input('How many candies can we take in one turn?\n '))
    first = int(input(
        f'{players[0]}, if you want to go first, press "1", if not, - any other key\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = r(1, rules[1])
            print(f'I pick up {move}')
        else:
            print(f'{players[0]}, {ch(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f"It's too much, you can take no more {rules[1]} of candies {letter}, we have only {rules[0]} candies{letter}")
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Try again, you have {attempt} attempts')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Sorry, you have no more attempts.. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'There are {rules[0]} sweets left{letter}')
        else:
            print('All sweets are disassembled.')
        count += 1
    return players[count % 2]


players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('We have no winner.(draw)')
else:
    print(f'Congratulations! This time {winer} won! He gets all the candy!')
