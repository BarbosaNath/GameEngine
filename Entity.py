class Entity(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.address = '0x'+hex(id(self)).upper()[2:]

    def add(self, component: str, value):
        self[component] = value
        return self

    def remove(self, component: str):
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
