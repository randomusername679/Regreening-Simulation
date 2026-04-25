import sys
import pygame
import moderngl

from configs import config

class Simulation():
    def __init__(self):
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)

        pygame.display.set_mode(config.WINDOW_SIZE, flags=pygame.OPENGL | pygame.DOUBLEBUF)

        self.context = moderngl.create_context()
        self.context.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE | moderngl.BLEND)
        self.context.gc_mode = "auto"

        self.clock = pygame.time.Clock()
        self.dt = 0
        self.time = 0

        self.running = False

    def update(self):
        self.dt = self.clock.tick()
        self.time = pygame.time.get_ticks() * 0.001
        pygame.display.set_caption(f"{self.clock.get_fps() :.0f}")

    def render(self):
        self.context.clear(color=config.BACKGROUND_COLOR)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = Simulation()
    app.run()
