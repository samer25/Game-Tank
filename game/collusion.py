import pygame

from game.setting_atributes import SettingAttributes

bullet_fired = False


class Collusion:
    def __init__(self):
        self.getting = SettingAttributes()
        self.offset_x = self.getting.bullet.position['x'] - self.getting.enemy.position['x']
        self.offset_y = self.getting.bullet.position['y'] - self.getting.enemy.position['y']
        self.offset_x_enemy = self.getting.bullet_enemy.position['x'] - self.getting.player.position['x']
        self.offset_y_enemy = self.getting.bullet_enemy.position['y'] - self.getting.player.position['y']
        self.overlap_player_with_bullet_enemy = self.getting.bullet.mask.overlap(self.getting.enemy.mask,
                                                                                 (self.offset_x, self.offset_y))
        self.overlap_enemy_with_bullet_enemy = self.getting.bullet_enemy.mask.overlap(self.getting.player.mask, (
            self.offset_x_enemy, self.offset_y_enemy))
        self.keys = pygame.key.get_pressed()

    def bullet_shoot(self):

        """if the key SPACE is press tank will shoot the bullet"""
        global bullet_fired
        if self.keys[pygame.K_SPACE]:
            bullet_fired = True
        elif self.getting.bullet.position['y'] < 0:
            """resetting position of bullet"""
            bullet_fired = False

        if bullet_fired:
            """if bullet is fired  moving the
            bullet by  decreasing the y position"""
            self.getting.bullet.position['y'] -= 5
        else:
            """if not bullet is in position of player"""
            self.getting.bullet.position['x'] = self.getting.player.position['x']
            self.getting.bullet.position['y'] = self.getting.player.position['y']

    def bullet_enemy_shoot(self):
        """setting the position of the bullet with correction - 13 of x position to be centered"""
        if self.getting.bullet_enemy.position['y'] < 700:
            self.getting.bullet_enemy.position['y'] += 5
        else:
            self.getting.bullet_enemy.position['x'] = self.getting.enemy.position['x'] - 13
            self.getting.bullet_enemy.position['y'] = self.getting.enemy.position['y']

    def collusion_with_enemy(self):
        global bullet_fired
        # See if the two masks at the offset are overlapping.
        """making over lap to return true if the bullet of enemy hit player """
        if self.overlap_player_with_bullet_enemy:
            self.getting.enemy.health['current'] -= self.getting.player.damage
            bullet_fired = False



    def collusion_with_player(self):
        # See if the two masks at the offset are overlapping.
        """making over lap to return true if the bullet of enemy hit player """

        if self.overlap_enemy_with_bullet_enemy:
            self.getting.player.health['current'] -= self.getting.enemy.damage
            self.getting.bullet_enemy.position['x'] = self.getting.enemy.position['x']
            self.getting.bullet_enemy.position['y'] = self.getting.enemy.position['y']

        if self.getting.enemy.is_dead:
            print(1)
