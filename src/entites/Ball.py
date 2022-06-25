from src.entites.Entity import Entity
from src.world.World import Border


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
