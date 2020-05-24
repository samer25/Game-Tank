"""importing the characters"""

from main_dir.drawing.Views import ViewPlayerTank, ViewEnemy, ViewBullet, ViewBulletEnemy
from main_dir.drawing.bullets import Bullets

"""importing the players to be set the  position health character and the position of health bar """

from main_dir.drawing.enemy_tank import EnemyTank
from main_dir.drawing.player import Player


class SettingAttributes:
    """setting the player position(x, y width height) health, character the position of health bar, correction of
    position hit box, size of hit box """
    player = Player(325, 560, 100, ViewPlayerTank.char, 7, [80, 50, 10], [37, 70], [13, 0])
    """setting the enemy position(x, y width height) health character and the position of health bar"""
    enemy = EnemyTank(325, 70, 100, ViewEnemy.char, 2, [-20, 50, 10], [40, 60], [5.5, -3])
    """setting the bullet position(x, y width height)"""
    bullet = Bullets(player.position['x'], player.position['y'], ViewBullet.bullet, [27, 17])
    """setting the enemy bullet position(x, y width height)"""
    bullet_enemy = Bullets(enemy.position['x'], enemy.position['y'], ViewBulletEnemy.bullet, [33, 28])
