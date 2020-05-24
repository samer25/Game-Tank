import pygame


class ViewPlayerTank:
    """loading the image of player character"""
    player_img = pygame.image.load('drawing/images/character.png')
    """scaling the image"""
    char = pygame.transform.scale(player_img, (60, 70))


"""loading the images for enemy character and changing the scale of image"""


class ViewEnemy:
    """loading the image of enemy character"""
    player_img = pygame.image.load('drawing/images/enemy_tank.png')
    """scaling the image"""
    char = pygame.transform.scale(player_img, (50, 60))


class ViewBullet:
    """loading the image of enemy character"""
    bullet_img = pygame.image.load('drawing/images/bullet.png')
    """scaling the image"""
    bullet = pygame.transform.scale(bullet_img, (50, 60))


class ViewBulletEnemy:
    """loading the image of enemy character"""
    bullet_img = pygame.image.load('drawing/images/e_bullet.png')
    """scaling the image"""
    bullet = pygame.transform.scale(bullet_img, (50, 60))


class BackgroundResources:
    """Background images"""
    background_images = (
        'drawing/images/bg.png', 'drawing/images/bg2.png', "drawing/images/bg3.png", "drawing/images/bg4.png",
        "drawing/images/bg5.png", "drawing/images/bg6.png",
        "drawing/images/bg7.png", "drawing/images/bg8.png", "drawing/images/bg9.png",
        "drawing/images/bg10.png", "drawing/images/bg11.png", "drawing/images/bg12.png", "drawing/images/bg13.png",
        "drawing/images/bg14.png",
        "drawing/images/bg15.png", 'drawing/images/bg2.png', 'drawing/images/bg4.png',
        "drawing/images/bg5.png", "drawing/images/bg1.png")

