from src.data.ImageLoader import load_image


class Border:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Entity:
    def __init__(self, texture_path, width, height):
        self.x = 0
        self.y = 0
        self.image = load_image(texture_path, width, height)

    def key_down(self, key):  # Abstract method
        pass

    def key_up(self, key):  # Abstract method
        pass

    def tick(self):  # Abstract method
        pass

    def render(self, scene):  # Abstract method
        pass


class Ball(Entity):
    def __init__(self):
        super().__init__("ball.png", 32, 32)
        self.border = Border(640, 320)

        rect = self.image.get_rect()  # self.image -> ball
        rect.x = self.border.width // 2
        rect.y = self.border.height // 2

    def tick(self):
        if rect.x > self.border.width or rect.x < 0:


    def render(self, scene):
        pass
