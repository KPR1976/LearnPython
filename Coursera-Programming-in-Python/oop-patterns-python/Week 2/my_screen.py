#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    """
    Класс для работы с 2-d векторами
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        """возвращает разность двух векторов"""
        return Vec2d(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + other.x, self.y + other.y)

    def len(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def dist(self, other):
        return (self - other).len()

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x * k, self.y * k)

    def int_pair(self):
        return int(self.x), int(self.y)

    def __str__(self):
        return '(x:{}, y:{})'.format(self.x, self.y)

    def __repr__(self):
        return '(x:{}, y:{})'.format(self.x, self.y)


class Polyline:
    """
    Класс для работы с ломанной линией
    """

    def __init__(self):
        self.base_points = []
        self.speeds = []

    def add_point(self, point, speed):
        self.base_points.append(point)
        self.speeds.append(speed)

    def delete_point(self, point):
        idx = self._get_nearest_base_point_idx(point)
        if idx is not None:
            self.base_points.pop(idx)
            self.speeds.pop(idx)

    def draw_base_points(self, gameDisplay, width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        for p in self.base_points:
            pygame.draw.circle(gameDisplay, color, p.int_pair(), width)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.base_points)):
            self.base_points[p] = self.base_points[p] + self.speeds[p]
            if self.base_points[p].x > SCREEN_DIM[0] or self.base_points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)

            if self.base_points[p].y > SCREEN_DIM[1] or self.base_points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def reset(self):
        self.base_points = []
        self.speeds = []

    def change_speed(self, k):
        for i in range(len(self.speeds)):
            self.speeds[i] *= k

    def _get_nearest_base_point_idx(self, point):
        min_dist = 10000000
        min_idx = None
        for i in range(0, len(self.base_points)):
            d = self.base_points[i].dist(point)
            if d < min_dist:
                min_dist = d
                min_idx = i
        return min_idx

    def draw(self, gameDisplay, width=3, color=(255, 255, 255)):
        self.draw_base_points(gameDisplay, width, color)


class Knot(Polyline):
    def __init__(self, steps=35):
        super().__init__()
        self.points = []
        self.steps = steps

    def steps_increase(self, diff):
        self.steps += diff
        if self.steps < 0:
            self.steps = 0

    def add_point(self, point, speed):
        super().add_point(point, speed)
        self.points = self.get_knot(self.base_points, self.steps)

    def delete_point(self, point):
        super().delete_point(point)
        self.points = self.get_knot(self.base_points, self.steps)

    def set_points(self):
        super().set_points()
        self.points = self.get_knot(self.base_points, self.steps)

    def reset(self):
        super().reset()
        self.points = []

    def draw(self, gameDisplay, width=3, color=(255, 255, 255)):
        self.draw_base_points(gameDisplay, width)
        for p_n in range(-1, len(self.points) - 1):
            pygame.draw.line(gameDisplay, color, self.points[p_n].int_pair(), self.points[p_n + 1].int_pair(), width)

    def _get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self._get_point(points, alpha, deg - 1) * (1 - alpha)

    def _get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self._get_point(base_points, i * alpha))
        return res

    def get_knot(self, points, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = [(points[i] + points[i + 1]) * 0.5, points[i + 1], (points[i + 1] + points[i + 2]) * 0.5]
            res.extend(self._get_points(ptn, count))
        return res


class KnotList:
    def __init__(self):
        self.knots = []
        self.selected = None

    def append(self, knot):
        self.knots.append(knot)
        self.selected = len(self.knots) - 1

    def draw(self, gameDisplay, width=3, color=(255, 255, 255)):
        for i in range(len(self.knots)):
            c = (255, 255, 255)
            if i == self.selected:
                c = color
            self.knots[i].draw(gameDisplay, width, c)

    def apply(self, func, *args, **kwargs):
        getattr(self.knots[self.selected], func)(*args, **kwargs)

    def set_points(self):
        for knot in self.knots:
            knot.set_points()

    def select_next(self):
        self.selected = (self.selected + 1) % len(self.knots)


# Функции отрисовки
# =======================================================================================
def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points in selected poly"])
    data.append(["Num-", "Less points in selected poly"])
    data.append(["M", "Increase speed of selected poly"])
    data.append(["L", "Decrease speed of selected poly"])
    data.append(["D", "Delete nearest point to the next left mouse click"])
    data.append(["N", "Create new poly"])
    data.append(["S", "Select next poly"])
    data.append(["", ""])
    data.append([str(knot.steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    knot = Knot(steps=35)
    knots = KnotList()
    knots.append(knot)
    show_help = False
    delete_pressed = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knots.apply('reset')
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    knots.apply('steps_increase', 1)
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    knots.apply('steps_increase', -1)
                if event.key == pygame.K_m:
                    knots.apply('change_speed', 2)
                if event.key == pygame.K_l:
                    knots.apply('change_speed', 0.5)
                if event.key == pygame.K_d:
                    delete_pressed = True
                if event.key == pygame.K_n:
                    knots.append(Knot())
                if event.key == pygame.K_s:
                    knots.select_next()

            if event.type == pygame.MOUSEBUTTONDOWN:
                point_pos = Vec2d(event.pos[0], event.pos[1])
                point_speed = Vec2d(random.random() * 2, random.random() * 2)
                if delete_pressed:
                    knots.apply('delete_point', point_pos)
                    delete_pressed = False
                else:
                    knots.apply('add_point', point_pos, point_speed)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        knots.draw(gameDisplay, color=color)

        if not pause:
            knots.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
