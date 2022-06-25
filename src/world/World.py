class World:
    def __init__(self, keylistener):
        self.entities = []
        self.keylistener = keylistener

    def register_entity(self, entity):
        self.entities.append(entity)

        self.keylistener.on_key_up.append(entity.key_up)
        self.keylistener.on_key_down.append(entity.key_down)

    def render(self, scene):
        for entity in self.entities:
            entity.render(scene)

    def tick(self):
        for entity in self.entities:
            entity.tick()
