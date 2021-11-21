import pygame, sys
import text as Text
import config as Config
from config import config


# pygame.init()
# screen = pygame.display.set_mode((500,500), pygame.DOUBLEBUF)
# clock  = pygame.time.Clock()


def act():
    pass

# Renderizar texto               X
# Renderizar botões              X
# Responder a botões             /
# Editar config.json
# link config file com debugui
# Desenhar config.json
# scroll bar

# Class ------------------------------------------------------------------------
class DebugUI(dict):
    def __init__(self, screen, position, size, font=Text.arial[16]):
        self.canvas = pygame.Surface(size, pygame.SRCALPHA)
        self.config = config
        self.font   = font
        self.size   = size
        self.screen = screen
        self.height = font.get_height()
        self.position = position

        # elementos do dict:
        # # ID
        # # Label
        # # Tipo (texto, botão, scroll, checkbox)
        # #

# Render all configs to screen -------------------------------------------------
    def render(self):
        self.canvas.fill((0x00000000))
        posX, posY = self.position
        width, height = self.size

        for i, id in enumerate(self):
            curheight  = i*self.height
            dubheight  = curheight+self.height
            halfheight = curheight+self.height//2
        # Type Text ------------------------------------------------------------
            if self[id]['type'] == 'text':
                Text.render(self.font, self[id]['label'],
                            self[id]['color'], (width//2 - self.font.size(self[id]['label'])[0]//2, curheight),self.canvas)

        # Type Button ----------------------------------------------------------
            if self[id]['type'] == 'button':
                rect     = pygame.Rect(   0,     curheight,width,self.height)
                realRect = pygame.Rect(posX,posY+curheight,width,self.height)

                # Hover --------------------------------------------------------
                self[id]['hover']=True if realRect.collidepoint(pygame.mouse.get_pos()) else False
                color = 'grey' if self[id]['hover'] else self[id]['color']

                # Click --------------------------------------------------------
                if self[id]['hover'] and pygame.mouse.get_pressed()[0] \
                                     and not self[id]['just_pressed']:
                    color = 'blue'
                    self[id]['action']('aaa')
                    self[id]['just_pressed'] = True
                elif not pygame.mouse.get_pressed()[0]:
                    self[id]['just_pressed'] = False

                # Draw square for button ---------------------------------------
                pygame.draw.rect(self.canvas,color,rect)
                Text.render(self.font, self[id]['label'],
                            'BLACK', (width//2 - self.font.size(self[id]['label'])[0]//2, curheight),self.canvas)

        # Type Checkbox --------------------------------------------------------
            if self[id]['type'] == 'checkbox':
                Text.render(self.font, self[id]['label'],
                            self[id]['color'], ( 0, curheight),self.canvas)

                size = (self.height**.8,  self.height**.8)

                pos  = (width - self.height + self.height*.25,
                        halfheight-self.height*.25)
                rect     = pygame.Rect((       pos[0],      pos[1]), size)
                realRect = pygame.Rect((posX + pos[0], posY+pos[1]), size)



                self[id]['hover']=True if realRect.collidepoint(pygame.mouse.get_pos()) else False
                color = 'grey' if self[id]['hover'] else self[id]['color']


                if self[id]['hover'] and pygame.mouse.get_pressed()[0] \
                                     and not self[id]['just_pressed']:
                    color = 'blue'
                    self[id]['on'] = not self[id]['on']
                    self[id]['action'](self[id]['on'])
                    self[id]['just_pressed'] = True
                elif not pygame.mouse.get_pressed()[0]:
                    self[id]['just_pressed'] = False

                if self[id]['on']:
                    Text.render(self.font, 'x', self[id]['color'],
                               (pos[0]+self.height//18,curheight-self.height//9), self.canvas)

                pygame.draw.rect(self.canvas,color,rect, 2)


        # Type Scroll ----------------------------------------------------------
            if self[id]['type'] == 'scroll':
                rnge=self[id]['range']
                # Horizontal line ----------------------------------------------
                pygame.draw.aaline(self.canvas, self[id]['color'], (1, halfheight), (width-1, halfheight))
                # Vertical lines -----------------------------------------------
                pygame.draw.aaline(self.canvas, self[id]['color'], (0,  curheight), (      0,  dubheight))
                pygame.draw.aaline(self.canvas, self[id]['color'], (width-1, curheight), (width-1, dubheight))

                # Integer divisor lines ----------------------------------------
                if rnge[1]-rnge[0] > self[id]['module']:
                    for i, x in enumerate(range(self[id]['range'][0], self[id]['range'][1])):
                        if i % self[id]['module'] == 0:
                            pygame.draw.aaline(self.canvas, self[id]['color'],
                                    (x * width//(self[id]['range'][1]-self[id]['range'][0]), curheight),
                                    (x * width//(self[id]['range'][1]-self[id]['range'][0]), dubheight))
                else:
                    for x in range(self[id]['range'][0], self[id]['range'][1]):
                        pygame.draw.aaline(self.canvas, self[id]['color'],
                                (x * width//(self[id]['range'][1]-self[id]['range'][0]), curheight),
                                (x * width//(self[id]['range'][1]-self[id]['range'][0]), dubheight))


                pos = ((self[id]['value']-self[id]['range'][0])*width//(self[id]['range'][1]-self[id]['range'][0]))-self.height//4
                # print(self[id]['value'])

                rect = ((pos,curheight),(self.height//2,self.height))
                realRect = pygame.Rect((posX,curheight+posY), (width, self.height))

                self[id]['hover']=True if realRect.collidepoint(pygame.mouse.get_pos()) else False
                color = 'grey' if self[id]['hover'] else self[id]['color']

                pygame.draw.rect(self.canvas,color,rect)



                if self[id]['hover'] and pygame.mouse.get_pressed()[0]:
                    self[id]['value'] = (((pygame.mouse.get_pos()[0]-posX)/width) * (rnge[1]-rnge[0])) + rnge[0]
                if self[id]['hover'] and pygame.mouse.get_pressed()[0] \
                                     and not self[id]['just_pressed']:
                    color = 'blue'
                    self[id]['just_pressed'] = True
                elif (not pygame.mouse.get_pressed()[0]) and self[id]['just_pressed']:
                    rnge=self[id]['range']
                    self[id]['value'] = (((pygame.mouse.get_pos()[0]-posX)/width) * (rnge[1]-rnge[0])) + rnge[0]
                    value=self[id]['value']
                    self[id]['value'] = rnge[1] if value > rnge[1] else value
                    value=self[id]['value']
                    self[id]['value'] = rnge[0] if value < rnge[0] else value

                    if self[id]['snappy']:
                        if self[id]['bignumbers']:
                            self[id]['value'] = round(self[id]['value']/10)*10
                        else:
                            self[id]['value'] = round(self[id]['value'])

                    self[id]['action'](self[id]['value'])
                    self[id]['just_pressed'] = False


                value=self[id]['value']
                if self[id]['value'] <= (self[id]['range'][1]-self[id]['range'][0])/2:
                    Text.render(self.font, f'{float(value):.1f}', 'YELLOW',
                                   (pos+self.height,curheight-self.height//9), self.canvas)
                else:
                    Text.render(self.font, f'{float(value):.1f}', 'YELLOW',
                                   (pos-self.height,curheight-self.height//9), self.canvas)
                del rnge


        # Draw canvas on screen
        self.screen.blit(self.canvas, self.position)

# Add config ---------------------------------------------------------------
    def add(self, id, link = None, type='text', label='', action=lambda x: act(), color='white', rnge=[0,10], snappy=True, module=10, bignumbers=False):
        self[id] = {'link'  :   link, 'type'  :   type,
                    'label' :  label, 'color' :  color,
                    'action': action, 'range' :   rnge,
                    'snappy': snappy, 'module': module,
                    'bignumbers':bignumbers}
        ## Type especifics -----------------------------------------------------
        # Button ---------------------------------------------------------------
        if type == 'button':
            self[id]['hover' ] = False
            self[id]['just_pressed'] = False
        # Checkbox -------------------------------------------------------------
        if type == 'checkbox':
            self[id]['on'] = False
            self[id]['hover' ] = False
            self[id]['just_pressed'] = False
        # Scroll ---------------------------------------------------------------
        if type == 'scroll':
            self[id]['value'] = rnge[0]
            self[id]['hover'] = False
            self[id]['just_pressed'] = False


    # def link(self):
    # def edit(self, id, text): pass


# debugUI.add('load', label='load', type='button', action=lambda x: Config.load())
# debugUI.add('save', label='save', type='button', action=lambda x: Config.save())
# debugUI.add('1', label='1')
# debugUI.add('2', label='2', type='button'  , action=lambda x: act(x))
# debugUI.add('3', label='3', type='checkbox', action=lambda x: act(x))
# debugUI.add('4', label='4', type='scroll'  , action=lambda x: act(x))


# while 1:
#     screen.fill(0x000000)
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT or \
#           (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
#             pygame.quit()
#             sys.exit()
#
#     debugUI.render(pygame.mouse.get_pos())
#
#     pygame.display.update()
#     clock.tick(60)
