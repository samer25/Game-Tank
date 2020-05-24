import pygame


class Bullets:
    def __init__(self, x, y, bullet, p_bullet_hit_box_correction):
        self.p_bullet_hit_box_correction = p_bullet_hit_box_correction
        self.bullet = bullet
        self.position = {"x": x, "y": y}
        self.mask = pygame.mask.from_surface(self.bullet)

    def redraw_bullet(self, win):
        """redraw the bullet and setting position of bullet by the player position"""
        win.blit(self.bullet, (self.position['x'] + 10, self.position['y']))
        """making hit box of bullet"""
        hit_box = (self.position['x'] + self.p_bullet_hit_box_correction[0],
                   self.position['y'] + self.p_bullet_hit_box_correction[1], 10, 20)
        pygame.draw.rect(win, (255, 0, 0), hit_box, 2)

    @property
    def bullet_fired(self):
        return False
