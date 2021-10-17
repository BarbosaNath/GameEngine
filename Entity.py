# class Entity:
#     def __init__(self, components=None, systems=None):
#         self.components = list()
#         self.systems    = list()
#
#         self.address = '0x'+hex(id(self)).upper()[2:]
#
#         self.add_component(components)
#         self.add_system(systems)
#
#     def add_component(self, components):
#         if isinstance(components, list) or isinstance(components, tuple):
#             for component in components: self.components.append(component )
#         elif components   is not   None: self.components.append(components)
#         return self
#
#     def add_system(self, systems):
#         if isinstance(systems, list) or isinstance(systems, tuple):
#             for system in systems: self.systems.append(system )
#         elif systems is not  None: self.systems.append(systems)
#         return self
#
#     def component(self, type):
#         for component in self.components:
#             if isinstance(component, type):
#                 return component
#         return None
#
#     def system(self, type):
#         for system in self.systems:
#             if isinstance(system, type): return system
#             else: return None
#
#     def update(self):
#         for system in self.systems:
#             system.update()

class Entity(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.address = '0x'+hex(id(self)).upper()[2:]

    def add(self, component, value):
        self[component] = value
        return self

    def remove(self, component):
        self.pop(componWent)
        return self

    def __repr__(self):
        str_text  = 'Entity('
        for i, item in enumerate(self.items()):
            str_text += f'{item[0]} = '

            str_text += repr(item[1])

            if i != len(self) - 1:
                str_text += ', '
        str_text += ')'
        return str_text

    def __str__(self):
        str_text = 'Entity object with '
        for i, key in enumerate(self.keys()):
            str_text += str(key)
            if   i == len(self.keys()) - 2: str_text += ' and '
            elif i != len(self.keys()) - 1: str_text += ', '
        return str_text

    def __getattr__(self, attribute):
        return self[attribute]
