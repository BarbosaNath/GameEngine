import pygame, sys
from random import randint

class Entity(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

class Attributes(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, attribute):
        return self[attribute]

    def __repr__(self):
        str_text = 'Attributes('
        for j, att in enumerate(self.items()):
            str_text += f'{att[0]}={repr(att[1])}'
            if j != len(self) - 1:
                str_text += ','
        str_text += ')'
        return str_text

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

class World(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self, dt):
        for system in self:
            self[system].update(dt)

class ParticleSystem:
    def __init__(self, entity_manager, canvas):
        self.entity_manager = entity_manager
        self.canvas = canvas

    def update(self, dt):
        for i, entity in enumerate(self.entity_manager):
            if 'PositionComponent' in entity and \
               'VelocityComponent' in entity and \
               'ParticleComponent' in entity and \
               'TimerComponent'    in entity:
                entity['PositionComponent']['x'] +=entity['VelocityComponent']['x']*dt*20
                entity['PositionComponent']['y'] +=entity['VelocityComponent']['y']*dt*20
                pygame.draw.circle(self.canvas, WHITE,
                                    (entity['PositionComponent']['x'],
                                     entity['PositionComponent']['y']),
                                 entity['TimerComponent']['timer'])
                entity['TimerComponent']['timer']-=entity['TimerComponent']['time']*dt*20
                if entity['TimerComponent']['timer'] <= 0:
                    del self.entity_manager[i]

pygame.init()

def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts


def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_fps():
    "Data that will be rendered and blitted in _display"
    render(
        fonts[0],
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))


fonts = create_fonts([32,16,14,8])

screen = pygame.display.set_mode((500, 500),pygame.DOUBLEBUF)
clock  = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,pygame.KEYUP])

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

seconds = 0.0

em = EntityManager()


world = World(ParticleSystem = ParticleSystem(em, screen))

while 1:
    mouse = pygame.mouse.get_pos()
    dt = clock.get_time()/1000.0

    screen.fill(BLACK)

    render(fonts[0], str(len(em)), 'white', (250,0))
    display_fps()

    world.update(dt)


    em.append(Entity(
                PositionComponent = {'x':250,'y':250},
                VelocityComponent = {'x':randint(0,200)/100-1,'y':randint(0,200)/100-1},
                ParticleComponent = {},
                TimerComponent    = {'timer':5,'time':.1}
            )
        )

    for e in pygame.event.get():
        if e.type == pygame.QUIT    or \
          (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
