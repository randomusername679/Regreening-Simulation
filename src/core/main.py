import pygame
import src.configs.config as config
from sys import exit
import mod

class Main:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(config.SCREEN_SIZE)
        self.display.fill(config.BACKGROUND_COLOR)

        self.clock = pygame.time.Clock()

        self.context = moderngl.create_context()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            dt = self.clock.tick() / 1000
            pygame.display.update()

if __name__ == "__main__":
    simulation = Main()
    simulation.run()