from sys import exit
import struct
import os

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

        self.context = moderngl.create_context(standalone=True)

        Main.moderngl_test()

    @staticmethod
    def moderngl_test():
        file = open("../shaders/test.glsl")
        shader = file.read()
        file.close()

        ctx = moderngl.create_context(standalone=True)
        program = ctx.program(
            vertex_shader=shader,
            varyings=("value", "product")
        )

        num_vertices = 10
        vao = ctx.vertex_array(program, [])
        buffer = ctx.buffer(reserve=num_vertices*8)
        vao.transform(buffer, vertices=num_vertices)
        data = struct.unpack("20f", buffer.read())
        for i in range(0, 20, 2):
            print("data = {} product = {}".format(*data[i:i+2]))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            static_dt = self.clock.tick() / 1000
            self.settings.update(static_dt)

            dt = static_dt * self.settings.time_scale

            # print(self.settings.visualise_mycorrhiza)

            pygame.display.update()

if __name__ == "__main__":
    simulation = Main()
    simulation.run()