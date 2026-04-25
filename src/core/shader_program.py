import moderngl

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.context = self.app.context

        self.quad = self.get_program(shader_name="quad")

        self.init_uniforms()

    def init_uniforms(self):
        pass

    def update(self):
        pass

    def get_program(self, shader_name: str) -> moderngl.Program:
        with open(f"../shaders/{shader_name}.vert") as shader:
            vertex = shader.read()

        with open(f"../shaders/{shader_name}.vert") as shader:
            fragment = shader.read()

        program = self.context.program(vertex_shader=vertex, fragment_shader=fragment)
        return program