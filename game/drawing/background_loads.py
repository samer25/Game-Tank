import pygame

from game.drawing.Views import BackgroundResources


class BackgroundLoads:
    def __init__(self):
        """getting Image from background resources It is a list of images"""
        self.image = BackgroundResources.background_images

    def load_and_move(self):
        """loading image"""
        background_images_load = pygame.image.load(self.image[0])
        """scaling the size of image"""
        view_background = pygame.transform.scale(background_images_load, (700, 700))
        return view_background
