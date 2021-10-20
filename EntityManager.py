class EntityManager(dict):
    def __init__(self): pass

    def all(self, filter=None):
        """ return all entities with an especific component """

        if filter is not None:
            newDict = {}
            for id in self:
                if filter in self[id]:
                    newDict[id]=self[id]

            return newDict
        else: return self
