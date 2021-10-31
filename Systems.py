import pygame
import os

# Particle System --------------------------------------------------------------
class ParticleSystem:
    def __init__(self, entity_manager, canvas):
        self.entity_manager = entity_manager
        self.canvas = canvas

    def update(self, dt):
        for id in self.entity_manager.all('ParticleComponent'):
            if 'PositionComponent' in self.entity_manager[id].keys() and \
               'VelocityComponent' in self.entity_manager[id].keys() and \
               'TimerComponent'    in self.entity_manager[id].keys():
                self.entity_manager[id]['PositionComponent']['x'] +=self.entity_manager[id]['VelocityComponent']['x']*dt*20
                self.entity_manager[id]['PositionComponent']['y'] +=self.entity_manager[id]['VelocityComponent']['y']*dt*20
                pygame.draw.circle(self.canvas, (255,255,255),
                                    (self.entity_manager[id]['PositionComponent']['x'],
                                     self.entity_manager[id]['PositionComponent']['y']),
                                 self.entity_manager[id]['TimerComponent']['timer'])

                self.entity_manager[id]['VelocityComponent']['x'] *= 0.99
                self.entity_manager[id]['VelocityComponent']['y'] *= 0.99

                self.entity_manager[id]['TimerComponent']['timer']-=self.entity_manager[id]['TimerComponent']['time']*dt*20
                if self.entity_manager[id]['TimerComponent']['timer'] <= 0:
                    del self.entity_manager[id]


# Control System ---------------------------------------------------------------
class ControlSystem:
    def __init__(self, entity_manager):
        self.entity_manager = entity_manager
        self.dirX = 0
        self.dirY = 0

    def update(self, dt):
        for i, entity in enumerate(self.entity_manager.values()):
            if 'ControllerComponent' in entity:
                if 'PositionComponent'  in entity and \
                   'VelocityComponent'  in entity and \
                   'DirectionComponent' in entity:

                    entity['DirectionComponent']['y'] = pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w]

                    entity['DirectionComponent']['x'] = pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a]

                    dir = entity['DirectionComponent']

                    if self.dirX != dir['x'] or self.dirY != dir['y']:
                        # os.system('cls')

                        self.dirX=dir['x']
                        self.dirY=dir['y']

                        text = ' ⤬ \n⤬⤬⤬'
                        #       0123 456
                        text = list(text)

                        if dir['y'] == -1: text[1] = 'w'
                        if dir['x'] == -1: text[4] = 'a'
                        if dir['y'] ==  1: text[5] = 's'
                        if dir['x'] ==  1: text[6] = 'd'

                        text=''.join(text)

                    debugLog.edit_line(1,'text',text)



# class MoveSystem:
# class RenderSystem:
