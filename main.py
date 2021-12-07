# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 360  # ширина игрового окна
HEIGHT = 480  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Рендеринг
    screen.fill(BLACK)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
