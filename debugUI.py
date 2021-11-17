import pygame, sys
import text as Text
import config
from config import config


pygame.init()
screen = pygame.display.set_mode((500,500), pygame.DOUBLEBUF)
clock  = pygame.time.Clock()


def act(teste):
    print(teste)

# Renderizar texto
# Renderizar botões
# Responder a botões
# Editar config.json
# link config file com debugui
# Desenhar config.json
# scroll bar

class DebugUI(dict):
    def __init__(self, screen, position, size, font=Text.arial[16]):
        self.canvas = pygame.Surface(size, pygame.SRCALPHA)
        self.config = config
        self.font   = font
        self.screen = screen
        self.position = position

        # elementos do dict:
        # # ID
        # # Label
        # # Tipo (texto, botão, scroll, checkbox)
        # # 

    def render(self, mouse):
        self.canvas.fill((0x00000000))
        posX, posY = self.position

        for i, id in enumerate(self):
            if self[id]['type'] == 'text':
                Text.render(self.font, self[id]['label'],
                            self[id]['action'], (0, i*20),self.canvas)

            if self[id]['type'] == 'button':
                rect     = pygame.Rect(   0,     i*20,20,20)
                realRect = pygame.Rect(posX,posY+i*20,20,20)

                self[id]['hover']=True if realRect.collidepoint(mouse) else False
                color = 'grey' if self[id]['hover'] else 'white'

                if self[id]['hover'] and pygame.mouse.get_pressed()[0] \
                                     and not self[id]['just_pressed']:
                    color = 'blue'
                    self[id]['action']()
                    self[id]['just_pressed'] = True

                elif not pygame.mouse.get_pressed()[0]:
                    self[id]['just_pressed'] = False

                pygame.draw.rect(self.canvas,color,rect)
        self.screen.blit(self.canvas, self.position)

    def add(self, id, link = None, type='text', label='', action=None):
        self[id] = {'link': link, 'type': type, 'label': label}
        if type == 'text':
            self[id]['action'] = 'white' if action is None else action

        if type == 'button':
            self[id]['hover' ] = False
            self[id]['action'] = action
            self[id]['just_pressed'] = False
    # def link(self):
    def edit(self, id, text): pass

dui = DebugUI(screen,(250, 250),(250,250))
# print(dui.config)
dui.add('teste ', label='1')
dui.add('teste2', label='2', type='button', action=lambda: act('aaaa'))


while 1:
    screen.fill(0x000000)
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
          (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    dui.render(pygame.mouse.get_pos())

    pygame.display.update()
    clock.tick(60)
