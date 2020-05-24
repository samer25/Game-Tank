import pygame

from main_dir.drawing.bullets import Bullets


class BulletEnemy(Bullets):
    def __init__(self, x, y, bullet, p_bullet_hit_box_correction):
        super().__init__(x, y, bullet, p_bullet_hit_box_correction)
