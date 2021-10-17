# class EntityManager:
#     def __init__(self, entities=None):
#         self.entities = list()
#
#         self.add(entities)
#
#     def add(self, entities):
#         if isinstance(entities, list) or isinstance(entities, tuple):
#             for entity in entities: self.entities.append(entity )
#         elif entities  is not None: self.entities.append(entities)
#
#     def remove(self, entity):
#         self.entities.remove(entity)
#
#     def update(self):
#         for entity in self.entities:
#             entity.update()

class EntityManager(list):
    def __init__(self): pass

    def all(self, filter=None):
        """
        return all entities with an especific component
        """

        if filter is not None:
            newList = []
            for item in self:
                if filter in item:
                    newList.append(item)

            return newList
        else:
            return self
