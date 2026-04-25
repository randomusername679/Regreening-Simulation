import numpy

from meshes.base_mesh import BaseMesh

class QuadMesh(BaseMesh):
    def __init__(self, app):
        self.app = app
        self.context = self.app.context
        self.program = self.app.shader_program.quad

        self.vbo_format = "3f 3f"
        self.attributes = ("in_position", "in_color")
        self.vao = self.get_vao()

    def get_vertex_data(self) -> numpy.array:
        vertices = [
            ( 0.5,  0.5,  0.0), (-0.5,  0.5,  0.0), (-0.5, -0.5,  0.0),
            ( 0.5,  0.5,  0.0), (-0.5, -0.5,  0.0), ( 0.5, -0.5,  0.0)
        ]

        colors = [
            (0, 1, 0), (1, 0, 0), (1, 1, 0),
            (0, 1, 0), (1, 1, 0), (0, 0, 1)
        ]

        vertex_data = numpy.hstack([vertices, colors], dtype="float32")
        return vertex_data
