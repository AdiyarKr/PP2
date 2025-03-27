import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Эллипс внутри")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Параметры эллипса
ellipse_center = (width // 2, height // 2)
ellipse_radius_x = 100
ellipse_radius_y = 50

# Основной цикл программы
running = True
while running:
    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(WHITE)

    # Нарисовать эллипс
    pygame.draw.ellipse(screen, BLUE, (ellipse_center[0] - ellipse_radius_x,
                                       ellipse_center[1] - ellipse_radius_y,
                                       2 * ellipse_radius_x, 2 * ellipse_radius_y))

    # Обновить экран
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()