from random import randint

print('Приветствую в игре "камушки"\n')
print()
print('Здесь тебе предстоит обыграть моего робота!')
print(
    'Правила очень просты: тебе нужно тактически подбирать ходы, чтобы оставить своему противнику последний камень. В этом вся суть игры!')
print('Куча камней генерируется случайно от 4 до 30')
print('За ход ты можешь взять 1, 2 или 3 камня')
print(f'ЖЕЛАЮ УДАЧИ!\n\n{"*" * 20}')

N = randint(4, 31)
print(f'** Изначально в кучке {N} камней **')

pl1 = 1
pl2 = -1
step = 0
while N > 0:
    if pl1 == 1:
        while not(1 <= step <= 3):
            try:
                print('Игрок 1, сделайте ход:\t')
                step = int(input())
            except ValueError:
                print('** Введите значение согласно условию! **')
            if not(1 <= step <= 3):
                print('** Введите значение согласно условию! **')

    if pl2 == 1:
        while not(1 <= step <= 3):
            try:
                print('Игрок 2, сделайте ход:\t')
                step = int(input())
            except ValueError:
                print('** Введите значение согласно условию! **')
            if not(1 <= step <= 3):
                print('** Введите значение согласно условию! **')
    N -= step
    pl1 = -1
    pl2 = 1
    step = 0
    print(f'** В куче {max(N,0)} камней **')

if pl1 == 1:
    print('** ИГРА ОКОНЧЕНА ВЫИГРАЛ ИГРОК 2 !!!')
else:
    print('** ИГРА ОКОНЧЕНА ВЫИГРАЛ ИГРОК 1 !!!')