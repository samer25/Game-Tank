import pygame

from main_dir.collusion import Collusion
from main_dir.drawing.background import BackGround

"""importing the moves of enemy"""
from main_dir.moves_of_object.enemy_moves import MovesEnemy

"""importing the moves of player"""

from main_dir.moves_of_object.player_move import PlayerMoves

from main_dir.setting_atributes import SettingAttributes

run = True

"""Main loop"""


def mainloop(running):
    clock = pygame.time.Clock()
    getting = SettingAttributes()
    pygame.init()
    screen = pygame.display.set_mode([700, 700])
    """the caption"""
    pygame.display.set_caption("Tank Game")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        """background"""
        BackGround().redraw_game_window(screen)
        if not getting.enemy.is_dead:
            """Moves of enemy"""
            MovesEnemy().moving_enemy()
            Collusion().bullet_enemy_shoot()
            """if enemy hit decrease health player"""
            Collusion().collusion_with_player()
            """redraw enemy tank"""
            getting.enemy.redraw_tank(screen)
            """redraw enemy bullet"""
            getting.bullet_enemy.redraw_bullet(screen)

        if not getting.player.is_dead:
            Collusion().bullet_shoot()
            """if enemy hit decrease health player"""
            Collusion().collusion_with_enemy()
            """redraw player tank"""
            getting.player.redraw_tank(screen)
            """redraw enemy bullet"""
            getting.bullet.redraw_bullet(screen)
            """player moves"""
            PlayerMoves().player_moves()
            Collusion().bullet_shoot()
        """updating screen"""
        pygame.display.update()

        """fps"""
        clock.tick(60)
    pygame.quit()


mainloop(run)
