"""importing player to create an enemy """

from game.drawing.player import Player

"""creating enemy is inherit from the Player class """


class EnemyTank(Player):
    """passing upon initialization position("x, y") of enemy, max health , the character enemy health position(x,
        y) and screen """

    def __init__(self, x, y, health, char, health_pos_x, health_y_width_height, size_of_hit_box,
                 correction_position_hit_box):
        super().__init__(x, y, health, char, health_pos_x, health_y_width_height, size_of_hit_box,
                         correction_position_hit_box)
        self.velocity = 2
        self.damage = 10


