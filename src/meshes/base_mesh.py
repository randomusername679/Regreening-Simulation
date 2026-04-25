import numpy
import moderngl

class BaseMesh:
    def __init__(self):
        # These none attributes should be initialized in the mesh class that inherits this
        self.context: moderngl.Context = None
        self.program = None

        self.vbo_format = None
        self.vao = None

        self.attributes: tuple[str, ...] = None

    def get_vertex_data(self) -> numpy.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.context.buffer(vertex_data)
        vao = self.context.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attributes)], skip_errors=True
        )

        return vao

    def render(self):
        self.vao.render()