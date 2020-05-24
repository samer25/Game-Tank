"""importing an enemy and player"""
import pygame

from game.moves_of_object.player_move import PlayerMoves

bullet_fired = False

"""moving auto an enemy"""
can_move = False


class MovesEnemy(PlayerMoves):
    def __init__(self):
        super().__init__()
        self.offset_x = self.getting.bullet_enemy.position['x'] - self.getting.player.position['x']
        self.offset_y = self.getting.bullet_enemy.position['y'] - self.getting.player.position['y']
        self.damage = 15
        self.overlap = self.getting.player.mask.overlap(self.getting.enemy.mask, (self.offset_x, self.offset_y))

    def moving_enemy(self):
        global can_move
        """when enemy is in 260 px can move right or if he is in 375 he can move left"""
        if self.getting.enemy.position["x"] < 260:
            can_move = True

        elif self.getting.enemy.position["x"] > 375:
            can_move = False

        """moving left increasing x position if he can move right or decreasing x position if he cant move left"""
        if can_move:
            self.getting.enemy.position["x"] += self.getting.enemy.velocity
        else:
            self.getting.enemy.position["x"] -= self.getting.enemy.velocity

