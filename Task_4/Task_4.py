# Напишите программу, которая по заданному номеру четверти, показывает
#  диапазон возможных координат точек в этой четверти (x и y).

number = int(input())

if (number == 1):
    print('X > 0 and Y > 0')

if (number == 4):
    print('X > 0 and Y < 0')

if (number == 3):
    print('X < 0 and Y < 0')

if (number == 2):
    print('X < 0 and Y > 0')