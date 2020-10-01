import pygame
from pygame.draw import *
import numpy as np

pygame.init()


def rec_angle(x1, y1, a, b, angle):
    """Вычисляет координаты вершин наклонного прямоугольника

    :param x1: координата x начальной точки
    :param y1: координата y начальной точки
    :param a: длина прямоугольника
    :param b: ширина прямоугольника
    :param angle: угол наклона
    :return: список кортежей координат вершин прямоугольника
    """
    angle = angle * np.pi / 180
    x2 = x1 + a * np.cos(angle)
    y2 = y1 + a * np.sin(angle)
    x3 = x1 + a * np.cos(angle) - b * np.sin(angle)
    y3 = y1 + a * np.sin(angle) + b * np.cos(angle)
    x4 = x1 - b * np.sin(angle)
    y4 = y1 + b * np.cos(angle)
    A = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    return A


FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (150, 150, 150), (0, 0, 400, 400), 0)
circle(screen, (255, 255, 0), (200, 175), 100, 0)
rect(screen, (0, 0, 0), (145, 220, 110, 25), 0)
circle(screen, (255, 0, 0), (160, 140), 20, 0)
circle(screen, (0, 0, 0), (160, 140), 10, 0)
circle(screen, (255, 0, 0), (250, 145), 18, 0)
circle(screen, (0, 0, 0), (250, 145), 8, 0)
polygon(screen, (0, 0, 0), rec_angle(120, 78, 90, 8, 35))
polygon(screen, (0, 0, 0), rec_angle(302, 95, 80, 8, 150))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

