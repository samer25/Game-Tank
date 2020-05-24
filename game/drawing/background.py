from game.drawing.background_loads import BackgroundLoads

"""getting the screen and setting background  """


class BackGround:
    """taking the image"""
    view_background = BackgroundLoads().load_and_move()

    def redraw_game_window(self, screen):
        """setting background in the screen at position x y"""
        screen.blit(self.view_background, (0, 0))
