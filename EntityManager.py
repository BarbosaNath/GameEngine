class EntityManager(dict):
    def __init__(self):
        self.all       = dict()
        self.available = list()
        self.id_count  = 0

    def add(self, entity):
        if self.available != []:
            id = self.available[0]
            del self.available[0]
        else:
            id = str(self.id_count)
            self.id_count += 1


        for component in entity:
            try:self.all[component].append(id)
            except:
                self.all[component]=list()
                self.all[component].append(id)


        self[id] = entity

    def remove(self, id):
        self.available.append(id)

        for component in self[id]:
            del self.all[component][self.all[component].index(id)]

        del self[id]

    def filter(self, filters):
        try: filtered = self.all[filters[0]]
        except: return []
        for i, filter in enumerate(filters):
            if i != 0:
                try: filtered = set(filtered).intersection(self.all[filter])
                except: return []
        return filtered
