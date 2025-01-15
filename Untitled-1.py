def multiplay(a,b):
    return a+b
def minus(a,b):
    return a-b
def umno(a, b):
    return a*b
def del_bez_ostatko(a, b):
    return a//b
def del_s_ostatkom(a, b):
    return a/b
def fack(a):
    cnt = 1
    for i in range(1, a+1):
        cnt *= i
    return cnt
def zodiac(year):
    animals = ["Крысы", "Быка", "Тигра", "Кролика", "Дракона", "Змеи", "Лощади", "Козы", "Обезьяны", "Петуха", "Собаки", "Свиньи"]
    start_year = 1900
    index = (year - start_year)%12
    return animals[index]
# import turtle 
# heart = turtle.Turtle()
# heart.color("red")
# heart.pensize(3)
# heart.speed(3)

def draw_heart():
    heart.begin_fill()
    heart.left(50)
    heart.forward(130)
    heart.circle(50, 200)
    heart.right(140)
    heart.circle(50, 200)
    heart.forward(130)
    heart.end_fill()
def generate_hashtag(s):
    #your code here
    hashtag = '#' + str(s.title().replace(' ', ''))
    return hashtag if 2 <= len(hashtag) <= 140 else False
import pygame
import time
import random

def gameLoop():
    pygame.init()
    dis_width, dis_height = 800, 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake game by Biibars')
    clock = pygame.time.Clock()
    snake_block, snake_speed = 10, 15
    snake_list, length_of_snake = [], 1
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT: x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP: y1_change, x1_change = -snake_block, 0
                elif event.key == pygame.K_DOWN: y1_change, x1_change = snake_block, 0

        x1 += x1_change
        y1 += y1_change
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: return

        dis.fill((50, 153, 213))
        pygame.draw.rect(dis, (0, 255, 0), [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        if any(block == snake_Head for block in snake_list[:-1]): return

        for block in snake_list:
            pygame.draw.rect(dis, (0, 0, 0), [block[0], block[1], snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Загрузка данных Tesla с Yahoo Finance
tesla = yf.Ticker("TSLA")
data = tesla.history(period="1y")  # Данные за последний год

# Визуализация цены закрытия
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Цена закрытия TSLA', color='blue')
plt.title('Исторические данные акций Tesla')
plt.xlabel('Дата')
plt.ylabel('Цена (USD)')
# plt.legend()
# plt.grid(True)
# plt.show()
print('''
    1 = плюс
    2 = минус
    3 = умножение
    4 = деление
    5 = деление без остатка
    6 = китайский год рождения   
    7 = факториал
    8 = нарисовать сердечко
    9 = создать #
    10 = змейка
    11 = цена акции Теслы
      ''')
# n = int(input("Выберите действие:" ))
# a = int(input('введите значение: '))
# b = int(input('введите значение: '))
while True:
    n = input("Выберите действие (или напишите 'stop' для выхода): ").strip()
    # a = int(input('введите значение: '))
    # b = int(input('введите значение: '))
    if n == 'stop':
        break  # Прерывание цикла при вводе "stop"
    
    n = int(n)  # Переходим к числовому значению действия

    if n == 1:
        a = int(input('введите значение: '))
        b = int(input('введите значение: '))
        result = multiplay(a, b)
        print(f'{a} + {b} = {result}')
    elif n == 2:
        a = int(input('введите значение: '))
        b = int(input('введите значение: '))    
        result = minus(a,b)
        print(f'{a} - {b} = {result}')
    elif n == 3:
        a = int(input('введите значение: '))
        b = int(input('введите значение: '))
        result = umno(a,b)
        print(f'{a} * {b} = {result}')
    elif n == 5:
        a = int(input('введите значение: '))
        b = int(input('введите значение: '))
        result = del_bez_ostatko(a,b)
        print(f'{a} // {b} = {result}')
    elif n == 4:
        a = int(input('введите значение: '))
        b = int(input('введите значение: '))
        result = del_s_ostatkom(a,b)
        print(f'{a} / {b} = {result}')
    
    elif n == 7:
        a = int(input('введите значение: '))
        result = fack(a)
        print(f"факториад {a} = {result}")
    elif n == 6:
        a = int(input('введите год рождения: '))
        result = zodiac(a)
        print(f'вы родились в год {result}')
    elif n == 8:
        import turtle 
        heart = turtle.Turtle()
        heart.color("red")
        heart.pensize(3)
        heart.speed(3)

        draw_heart()
    elif n == 9:
        a = input('Введите ваше слово: ')
        result = generate_hashtag(a)
        print(result)
    elif n == 10:
        gameLoop()
    elif n == 11:
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print('Errorinvidialtype {n}')











