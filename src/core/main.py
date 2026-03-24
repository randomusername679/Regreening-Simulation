from sys import exit

import pygame
import moderngl

import src.configs.config as config
from uitl.settings_handler import SettingsHandler

class Main:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(config.SCREEN_SIZE)
        self.display.fill(config.BACKGROUND_COLOR)

        self.clock = pygame.time.Clock()

        self.settings = SettingsHandler(self)

        # self.context = moderngl.create_context()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            static_dt = self.clock.tick() / 1000
            self.settings.update(static_dt)

            dt = static_dt * self.settings.time_scale

            print(self.settings.visualise_mycorrhiza)

            pygame.display.update()

if __name__ == "__main__":
    simulation = Main()
    simulation.run()