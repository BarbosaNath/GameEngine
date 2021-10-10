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

class EntityManager(dict):
    # add entities
    # access entities
    # filter entities
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def all_with(self, filter):
        # return todos as entidades com um componente
        return self.filter(lambda x: filter in x, self)

class World:
    # add systems
    # access systems
    # call systems update
    def __init__(self): pass
    def update(self):
        for system in self:
            system.update()

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


fonts= create_fonts([32,16,14,8])

screen = pygame.display.set_mode((500, 500),pygame.DOUBLEBUF)
clock  = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,pygame.KEYUP])

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

seconds = 0.0

em = list()
test = list()

while 1:
    mouse = pygame.mouse.get_pos()
    dt = clock.get_time()/1000.0

    seconds += dt
    if seconds  >= 0.1:
        for pixel in range(25):
            em.append(Entity(PositionComponent = {'x':pixel*20, 'y':500},
                             VelocityComponent = {'x':randint(0,200)/100 -1,'y':randint(0,400)/100-4},
                             TimerComponent    = {'timer':randint(2,6)})
                     )
        seconds=0

    screen.fill(BLACK)

    for particle in em:
        c = particle['TimerComponent']['timer']
        c = (50*c,15*c,5*c)
        def a(b):
            if b > 255: b=255
            return b

        c = tuple(map(a, c))

        if particle['TimerComponent']['timer'] <= 2.5: # Grey
            c = particle['TimerComponent']['timer']
            c = (15*c,15*c,15*c)
            c = tuple(map(a, c))

        if particle['TimerComponent']['timer'] >= 5.3: # Red
            c = particle['TimerComponent']['timer']
            c = (50*c,20*c,5*c)
            c = tuple(map(a, c))

        if particle['TimerComponent']['timer'] >= 5.7: # Yellow
            c = particle['TimerComponent']['timer']
            c = (40*c,40*c,20*c)
            c = tuple(map(a, c))


        particle['PositionComponent']['x']  += particle['VelocityComponent']['x']*dt*20
        particle['PositionComponent']['y']  += particle['VelocityComponent']['y']*dt*20
        particle['TimerComponent']['timer'] -= .05*dt*20
        pygame.draw.circle( screen, c,
                            (   particle['PositionComponent']['x'],
                                particle['PositionComponent']['y']
                            ),  particle['TimerComponent']['timer'])
        if particle['TimerComponent']['timer'] <= 0:
            em.remove(particle)



    render(fonts[0], str(len(em)), 'white', (250,0))
    display_fps()


    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)
