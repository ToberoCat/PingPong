from src.entites.Entity import Entity


class Bracket(Entity):
    def __init__(self):
        super().__init__("bracket.png", 32, 96)

    def get_movement(self):  # Abstract method
        return 0  # -1 -> Go down; 0 Stay, 1 Go up


class PlayerBracket(Bracket):
    def key_down(self, key):
        pass

    def key_up(self, key):
        pass

    def get_movement(self):
        return 0


class AIBracket(Bracket):
    def get_movement(self):
        return 0
