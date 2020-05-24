import pygame

"""importing ViewBackgroundImage to get the screen"""

"""Main character that will be controlled by the user"""


class Player:
    """passing upon initialization position("x, y") of player, max health , the character health position(x,
    y) and screen """

    def __init__(self, x, y, health, char, health_pos_x, health_y_width_height, size_of_hit_box,
                 correction_position_hit_box):
        self.correction_position_hit_box = correction_position_hit_box
        self.size_of_hit_box = size_of_hit_box
        self.char = char
        self.position = {"x": x, "y": y}
        self.max_health = health
        """current health with width for drawing health bar"""
        self.health = {"current": self.max_health, "width": 50}
        self.health_y_width_height = health_y_width_height
        self.health_pos_x = health_pos_x
        self.velocity = 2
        self.mask = pygame.mask.from_surface(self.char)
        self.damage = 20

    """putting player character and heath bar in the screen with setting the position """

    def redraw_tank(self, win):
        """putting character in the screen with position(x, y)"""
        win.blit(self.char, (self.position['x'], self.position['y']))
        """hitbox setting current position (x, y) with correction"""
        hit_box = (self.position['x'] + self.correction_position_hit_box[0],
                   self.position['y'] + self.correction_position_hit_box[1], self.size_of_hit_box[0],
                   self.size_of_hit_box[1])
        pygame.draw.rect(win, (255, 0, 0), hit_box, 2)
        # Health
        """drawing the under green health bar with red setting position that will follow the character"""
        pygame.draw.rect(win, (255, 0, 0),
                         (self.position['x'] + self.health_pos_x, self.position['y'] + self.health_y_width_height[0],
                          self.health_y_width_height[1], self.health_y_width_height[2]))
        """drawing the health with green and setting position of health bar and setting the character position health 
        bar to be stuck with character """
        pygame.draw.rect(win, (0, 128, 0),
                         (self.position['x'] + self.health_pos_x, self.position['y'] + self.health_y_width_height[0],
                          self.health_percent(), self.health_y_width_height[2]))

    """calculating the health bar with max health , current health and the width to be present   """

    def health_percent(self):
        return int(
            max(min(self.health['current'] / float(self.max_health) * self.health['width'], self.health['width']),
                0))

    @property
    def is_dead(self):
        if self.health['current'] <= 0:
            return True
        return False
