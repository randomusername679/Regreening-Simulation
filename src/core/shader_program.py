class ShaderProgram:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def get_shader_content(path: str) -> str:
        with open(path) as file:
            content = file.read()
            file.close()
        return content