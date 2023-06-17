#Pygame
import random

import pygame
pygame.init()
blue = (0, 0, 255) # код синего цвета
red = (255, 0, 0)
white = (255, 255, 255)
black = (0,0,0)

dis = pygame.display.set_mode((800, 500)) # размер окна
pygame.display.set_caption("Snake")
# скорость змейки
step = 10

# звуки
eating_sound = pygame.mixer.Sound('eat_apple.mp3')
game_over_sound = pygame.mixer.Sound('game_over.mp3')

game_over = False # флажок проигрыша

window_size = pygame.display.get_window_size()
# координаты змейки
x_1 = 100 # координата по горизонтали
y_1 = 400 # коорд по вертикале
x_1_change = 0 # шаг змейки
y_1_change = 0 # шаг по вертикале

# коорд яблока
apple_x = random.randrange(0, window_size[0], 10) # используем randrange потому что здесь можно указать шаг (10)
apple_y = random.randrange(0, window_size[1], 10)
# создаем переменную clock, отслеживаем время в игре
clock = pygame.time.Clock()

score = 0 # счетчик очков
font = pygame.font.Font(None, 36) # объект класса Font

# список координат препятствий
obstacles = []
for i in range(5):
    obstacle_x = random.randrange(0, window_size[0], 10)
    obstacle_y = random.randrange(0, window_size[1], 10)
    obstacles.append((obstacle_x, obstacle_y))


while not game_over: # начало основного цикла игры
    for event in pygame.event.get(): # цикл обработки событий
        if event.type == pygame.QUIT: # проверяем является текущее событие выход
            game_over_sound.play()
            game_over = True

        if event.type == pygame.KEYDOWN: #
            if event.key == pygame.K_LEFT: # если нажата клавиша стрелка влево
                x_1_change = -step
                y_1_change = 0
        if event.type == pygame.KEYDOWN: #
            if event.key == pygame.K_RIGHT: # если нажата клавиша стрелка влево
                x_1_change = step
                y_1_change = 0
        if event.type == pygame.KEYDOWN: #
            if event.key == pygame.K_UP: # если нажата клавиша стрелка влево
                y_1_change = -step
                x_1_change = 0
        if event.type == pygame.KEYDOWN: #
            if event.key == pygame.K_DOWN: # если нажата клавиша стрелка влево
                y_1_change = step
                x_1_change = 0

    if x_1 >= window_size[0] or y_1 >= window_size[1] or x_1 <= 0 or y_1 <= 0:
        game_over_sound.play(loops=1, maxtime=2000)
        #ждем окончания проигрывания
        pygame.time.wait(1000)
        game_over = True



    else:
        x_1 += x_1_change # изм факт коорд змейки
        y_1 += y_1_change

    dis.fill(white)

    for obstacle in obstacles:
        pygame.draw.rect(dis, black, [obstacle[0], obstacle[1], 10, 10]) # отрисовка препятствий


    nadpis = font.render("Очки: " + str(score), True, red) # создали переменную надпись
    dis.blit(nadpis, (10, 10))
    pygame.draw.rect(dis, blue, [x_1, y_1, 10, 10]) # отрисовка прямоугольника синего цвета на игр экране
    pygame.draw.rect(dis, red, [apple_x, apple_y, 10, 10])  # отрисовка яблока
    pygame.display.update() # обновление экрана

    if x_1 == apple_x and y_1 == apple_y:
        score += 1
        eating_sound.play()
        apple_x = random.randrange(0, window_size[0], 10)  # используем randrange потому что здесь можно указать шаг (10)
        apple_y = random.randrange(0, window_size[1], 10)
        # величиваем скорость змейки, если счетчик кратен 10
        if score % 10 == 0:
            step += 10

    for obstacle in obstacles:
        if x_1 == obstacle[0] and y_1 == obstacle[1]:
            game_over_sound.play(loops=1, maxtime=2000)
            # ждем окончания проигрывания
            pygame.time.wait(1000)
            game_over = True

    clock.tick(20) # ограничение кадров в секунду


pygame = quit() # выход из игры
quit() # выход из программы

#ДЗ на понедельник (Ivanov_Lesson_23.py)
# 1. Увеличить змейку после поедания каждого яблока
# 2. Увеличить очки после каждого съеденного яблока +
# 3. Усложнять игру по мере поедания яблок +
# 4. Добавить препятствия +
# 5. Игра заканчивается, если змейка врежется в свой хвост
# 6. Добавить звуки поедания яблок и game over +
