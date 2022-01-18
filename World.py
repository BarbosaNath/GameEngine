class World(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self, dt):
        for system in self:
            self[system].update(dt)
