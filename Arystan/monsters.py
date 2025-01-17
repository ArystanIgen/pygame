from pygame import *
import pyganim
import os
import pygame
MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = "#2110FF"
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_MONSTERHORYSONTAL = [('%s/blocks/skelet_l1.png' % ICON_DIR),
                               ('%s/blocks/skelet_l2.png' % ICON_DIR)]


class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft, maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(Color(MONSTER_COLOR))
        self.startX = x  # начальные координаты
        self.startY = y
        self.maxLengthLeft = maxLengthLeft  # максимальное расстояние, которое может пройти в одну сторону
        self.maxLengthUp = maxLengthUp  # максимальное расстояние, которое может пройти в одну сторону, вертикаль
        self.xvel = left  # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = up  # скорость движения по вертикали, 0 - не двигается
        boltAnim = []
        for anim in ANIMATION_MONSTERHORYSONTAL:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()
        self.health = 100

    def update(self, platforms,projectilegroup):  # по принципу героя

        self.image.fill(Color(MONSTER_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        self.rect.y += self.yvel
        self.rect.x += self.xvel
        self.collide(platforms,projectilegroup)
        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel = -self.xvel  # если прошли максимальное растояние, то идет в обратную сторону
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel  # если прошли максимальное растояние, то идет в обратную сторону, вертикаль

        if self.health <= 0:
            self.kill()

    def collide(self, platforms,projectilegroup):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:  # если с чем-то или кем-то столкнулись
                self.xvel = - self.xvel  # то поворачиваем в обратную сторону
                self.yvel = - self.yvel
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self, j):
                self.xvel=0
                self.kill()


