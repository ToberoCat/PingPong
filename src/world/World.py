class World:
    def __init__(self):
        self.entities = []

    def render(self, scene):
        for entity in self.entities:
            entity.render(scene)

    def tick(self):
        for entity in self.entities:
            entity.tick()
