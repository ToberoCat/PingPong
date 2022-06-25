from src.entites.Entity import Entity
from src.world.World import Border


class Ball(Entity):
    def __init__(self, width, height):
        super().__init__("ball.png", 32, 32)
        self.border = Border(width, height)

        self.x = self.border.width / 2
        self.y = self.border.height / 2

    def tick(self):
        # if rect.x > self.border.width or rect.x < 0:
        pass
