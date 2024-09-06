import pygame  # Подключение библиотеки

pygame.init()  # Подключение библиотеки
screen = pygame.display.set_mode((700, 700))  # Размер экрана
pygame.display.set_caption("Play_clicker")  # Название игры
pygame.display.set_icon(pygame.image.load('pictures/Icon.png'))  # Иконка игры

clicker = pygame.image.load('pictures/Panda.png')  # Кликер
DEFAULT_IMAGE_SIZE = (510, 500)  # Размер кликера
clicker = pygame.transform.scale(clicker, DEFAULT_IMAGE_SIZE)  # Размер кликера
square = pygame.Surface((400, 400))  # Размер кликера
square.fill((80, 0, 8))  # Цвет кликера
background = pygame.image.load('pictures/Bamboo.png')  # Фон
coins = pygame.image.load('pictures/Coins.png')  # Монеты
level_button = pygame.image.load('pictures/Level.png')  # Уровень

font_1 = pygame.font.Font('fonts/Roboto-Black.ttf', 40)  # Шрифт
font_2 = pygame.font.Font('fonts/Roboto-Black.ttf', 20)  # Шрифт

file = open('files_saves/Play_clicker_save.txt', 'r')  # Открытие файла

PandaCoins = int(file.readline())  # Монеты
level = int(file.readline(1))  # Уровень
time = 0  # Время между атовтодобычей

sound_click = pygame.mixer.Sound('sounds/Click.mp3')  # Звук клика
background_sound = pygame.mixer.Sound('sounds/ChineseBgMusic.mp3')  # Фоновая музыка
background_sound.play(-1)  # Фоновая музыка

running = True  # Работа игры
while running:
    time += 1
    if time == 250:
        time = 0
        PandaCoins += level

    screen.blit(background, (0, 0))  # Обновление экрана/фон
    screen.blit(coins, (20, 80))  # Монеты
    screen.blit(square, (150, 230))  # Кликер
    screen.blit(clicker, (100, 200))  # Кликер

    if PandaCoins >= 99999999999:  # Максимум монет
        PandaCoins = 99999999999  # Максимум монет
    screen.blit(font_1.render(f'{PandaCoins}', True, 'White'), (125, 100))  # Кол-во монет

    if level < 5:
        screen.blit(font_2.render(f'Уровень автодобычи - {level}lvl', True, 'White'), (400, 40))  # Уровень
        screen.blit(font_1.render(f' - {(level + 1) * 150}', True, 'White'), (450, 100))  # Цена повышения уровня
        screen.blit(level_button, (400, 80))  # Кнопка повышения уровня
    else:
        screen.blit(font_2.render(f'Уровень автодобычи - max lvl', True, 'White'), (400, 40))  # Уровень

    pygame.display.update()  # Обновление экрана
    square.set_alpha(255)  # Прозрачность кликера
    clicker.set_alpha(255)  # Прозрачность кликера

    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # Нажата ли кнопка
            if event.button == 1:  # Нажата ли левая кнопка
                mouse_pos = pygame.mouse.get_pos()  # Позиция мыши
                if 150 <= mouse_pos[0] <= 550 and 230 <= mouse_pos[1] <= 630:  # Нахоодится ли мышь в кликере
                    PandaCoins += 1  # Счётчик
                    square.set_alpha(20)  # Прозрачность кликера
                    clicker.set_alpha(20)  # Прозрачность кликера
                    sound_click.play()  # Звук клика

                if 400 <= mouse_pos[0] <= 455 and 80 <= mouse_pos[1] <= 152:  # Нахоодится ли мышь в повышение уровня
                    if level < 5:  # Максимальный уровень
                        if PandaCoins >= (level + 1) * 150:  # Хватает ли монет
                            PandaCoins -= (level + 1) * 150  # Минус монеты
                            level += 1  # Повышение уровня
        # Закрытие игры
        if event.type == pygame.QUIT:
            running = False
            file = open('files_saves/Play_clicker_save.txt', 'w')  # Перезапись файла
            file.writelines([str(PandaCoins) + '\n', str(level)])  # Сохранение
            file.close()  # Закрытие файла
            pygame.quit()  # Закрытие игры
