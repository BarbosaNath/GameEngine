class EntityManager:
    def __init__(self, entities=None):
        self.entities = list()

        self.add(entities)

    def add(self, entities):
        if isinstance(entities, list) or isinstance(entities, tuple):
            for entity in entities: self.entities.append(entity )
        elif entities  is not None: self.entities.append(entities)

    def remove(self, entity):
        self.entities.remove(entity)

    def update(self):
        for entity in self.entities:
            entity.update()
