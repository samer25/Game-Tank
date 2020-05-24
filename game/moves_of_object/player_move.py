import pygame


"""importing the player for attributes"""
from game.setting_atributes import SettingAttributes


class PlayerMoves:

    def __init__(self):
        self.keys = pygame.key.get_pressed()
        """getting the player and the bullet"""
        self.getting = SettingAttributes()

    def player_moves(self):
        """To work the key when you preset"""
        """when the player press left key decreasing x position if the player position is more that 260"""
        if self.keys[pygame.K_LEFT] and self.getting.player.position["x"] > 260:
            # if key left is pressed moving position left
            self.getting.player.position["x"] -= self.getting.player.velocity
        """when the player press right key increasing x position if the player position is less that 375"""

        if self.keys[pygame.K_RIGHT] and self.getting.player.position["x"] < 375:
            self.getting.player.position["x"] += self.getting.player.velocity
        """Bullet move with player"""
