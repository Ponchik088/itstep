import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой кликер")

# Определение переменных
score = 0
click_power = 1
spawn_time = 1.0  # время между появлениями кругов в секундах
circle_lifetime = 5.0  # время, в течение которого круг будет отображаться на экране в секундах
last_spawn_time = 0.0
circles = []

# Определение функций
def draw_text(text, font_size, x, y, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def spawn_circle():
    global last_spawn_time
    current_time = pygame.time.get_ticks() / 1000  # текущее время в секундах
    if current_time - last_spawn_time >= spawn_time:
        radius = random.randint(20, 100)
        x = random.randint(radius, SCREEN_WIDTH - radius)
        y = random.randint(radius, SCREEN_HEIGHT - radius)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = pygame.draw.circle(screen, color, (x, y), radius)
        circles.append((circle, current_time))
        last_spawn_time = current_time

def remove_expired_circles():
    current_time = pygame.time.get_ticks() / 1000  # текущее время в секундах
    for circle, spawn_time in circles:
        if current_time - spawn_time >= circle_lifetime:
            circles.remove((circle, spawn_time))

# Главный цикл игры
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for circle, spawn_time in circles:
                if circle.collidepoint(pos):
                    circles.remove((circle, spawn_time))
                    score += click_power

    # Отрисовка экрана
    screen.fill(BLACK)
    draw_text(f"Счёт: {score}", 36, SCREEN_WIDTH // 2, 50, WHITE)
    draw_text(f"Мощность клика: {click_power}", 24, SCREEN_WIDTH // 2, 100, WHITE)
    spawn_circle()
    remove_expired_circles()
    for circle, spawn_time in circles:
        current_time = pygame.time.get_ticks() / 1000  # текущее время в секундах
        if current_time - spawn_time < circle_lifetime:
            pygame.draw.circle(screen, circle.color, circle.center, circle.radius)

    pygame.display.flip()

    # Ограничение количества кадров в секунду
    clock.tick(FPS)

    # Завершение Pygame
pygame.quit()
