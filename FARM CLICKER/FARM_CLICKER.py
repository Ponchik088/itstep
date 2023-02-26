import pygame
import random

# Инициализация Pygame
pygame.init()

money = 10
house1_count = 0
house1_earnings = 0
house1_curprice = 10

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 560
FPS = 60

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((30,30,30))
pygame.display.set_caption("Простой кликер")

# Определение параметров кнопки
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
COINS_LABEL = f" = {money}"

# Загрузка изображения
image1 = pygame.image.load("farm1.png")
image2 = pygame.image.load("farm2.png")
image3 = pygame.image.load("farm3.png")
image4 = pygame.image.load("farm4.png")
image5 = pygame.image.load("farm5.png")
coin_image = pygame.image.load("coin.png")

# Изменение размера изображения
image1 = pygame.transform.scale(image1, (BUTTON_WIDTH, BUTTON_HEIGHT))
image2 = pygame.transform.scale(image2, (BUTTON_WIDTH, BUTTON_HEIGHT))
image3 = pygame.transform.scale(image3, (BUTTON_WIDTH, BUTTON_HEIGHT))
image4 = pygame.transform.scale(image4, (BUTTON_WIDTH, BUTTON_HEIGHT))
image5 = pygame.transform.scale(image5, (BUTTON_WIDTH, BUTTON_HEIGHT))
coin_image = pygame.transform.scale(coin_image, (50, 50))

# Создание кнопки
button_rect1 = pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image1, button_rect1)
button_rect2 = pygame.Rect(10, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image2, button_rect2)
button_rect3 = pygame.Rect(10, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image3, button_rect3)
button_rect4 = pygame.Rect(10, 340, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image4, button_rect4)
button_rect5 = pygame.Rect(10, 450, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image5, button_rect5)

screen.blit(coin_image, (SCREEN_WIDTH//2, 10))

font = pygame.font.Font("Roboto-Regular.ttf", 24)
text = font.render(COINS_LABEL, True, (255,255,255))
screen.blit(text, (SCREEN_WIDTH//2+50, 20))

house1_label = font.render(f"Кол-во: {house1_count}\n"
                           f"Сумм добыча: {house1_earnings}\n"
                           f"Стоимость: {house1_curprice}", True, (255,255,255))
screen.blit(house1_label, (button_rect1.x+110, button_rect1.y))


# Бесконечный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Обработка события нажатия кнопки
            if button_rect1.collidepoint(event.pos):
                print("Кнопка 1 нажата!")
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 2 нажата!")
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 3 нажата!")
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 4 нажата!")
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 5 нажата!")

    # Отрисовка экрана
    pygame.display.update()

    # Ограничение частоты обновления экрана
    pygame.time.Clock().tick(FPS)

# Завершение Pygame
pygame.quit()
