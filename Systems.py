import pygame, os
from Entity import Entity
from EntityManager import EntityManager
from math import cos, sin
from random import randint
from config import config

# Particle System --------------------------------------------------------------
class ParticleSystem:
    def __init__(self, entity_manager: EntityManager, canvas: pygame.Surface, layer2: pygame.Surface):
        self.entity_manager = entity_manager
        self.canvas = canvas
        self.canvas2 = layer2

    def update(self, dt):
        for id in self.entity_manager.filter(('ParticleComponent',
                                              'PositionComponent',
                                              'VelocityComponent',
                                              'TimerComponent')):

            self.entity_manager[id]['PositionComponent']['x'] +=self.entity_manager[id]['VelocityComponent']['x']*20*dt
            self.entity_manager[id]['PositionComponent']['y'] +=self.entity_manager[id]['VelocityComponent']['y']*20*dt


            if config['bloom']:
                pygame.draw.circle(self.canvas2, (255,0,0),
                    (self.entity_manager[id]['PositionComponent']['x'],
                    self.entity_manager[id]['PositionComponent']['y']),
                    self.entity_manager[id]['TimerComponent']['timer']*1.3)
                pygame.draw.circle(self.canvas2, (255,200,200),
                    (self.entity_manager[id]['PositionComponent']['x'],
                    self.entity_manager[id]['PositionComponent']['y']),
                    self.entity_manager[id]['TimerComponent']['timer']*1.2)
                # self.canvas2.set_alpha(64)
            pygame.draw.circle(self.canvas, (255,255,255),
                                (self.entity_manager[id]['PositionComponent']['x'],
                                 self.entity_manager[id]['PositionComponent']['y']),
                               self.entity_manager[id]['TimerComponent']['timer'])


            self.entity_manager[id]['VelocityComponent']['x'] *= 0.99
            self.entity_manager[id]['VelocityComponent']['y'] *= 0.99

            self.entity_manager[id]['TimerComponent']['timer']-=self.entity_manager[id]['TimerComponent']['time']*20*dt
            if self.entity_manager[id]['TimerComponent']['timer'] <= 0:
                self.entity_manager.remove(id)


# <> Control System ---------------------------------------------------------------
# class ControlSystem:
#     def __init__(self, entity_manager):
#         self.entity_manager = entity_manager
#         self.dirX = 0
#         self.dirY = 0
#
#     def update(self, dt):
#         for i, entity in enumerate(self.entity_manager.values()):
#             if 'ControllerComponent' in entity:
#                 if 'PositionComponent'  in entity and \
#                    'VelocityComponent'  in entity and \
#                    'DirectionComponent' in entity:
#
#                     entity['DirectionComponent']['y'] = pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w]
#
#                     entity['DirectionComponent']['x'] = pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a]
#
#                     dir = entity['DirectionComponent']
#
#                     if self.dirX != dir['x'] or self.dirY != dir['y']:
#                         # os.system('cls')
#
#                         self.dirX=dir['x']
#                         self.dirY=dir['y']
#
#                         text = ' ⤬ \n⤬⤬⤬'
#                         #       0123 456
#                         text = list(text)
#
#                         if dir['y'] == -1: text[1] = 'w'
#                         if dir['x'] == -1: text[4] = 'a'
#                         if dir['y'] ==  1: text[5] = 's'
#                         if dir['x'] ==  1: text[6] = 'd'
#
#                         text=''.join(text)
# </>


class ParticleSpawnerSystem:
    def __init__(self, em: EntityManager):
        self.entity_manager = em
        self.elapsed = 0

    def update(self, dt):
        self.elapsed += dt
        # particleList = self.entity_manager.filter(('ParticleComponent',
        #                                       'PositionComponent',
        #                                       'VelocityComponent',
        #                                       'TimerComponent'))
        for id in self.entity_manager.filter(('ParticleSpawner','Position')):
            e = self.entity_manager[id]



            # Particle ---------------------------------------------------------
            # while len(particleList) <= 20:
            if self.elapsed >= config['particles']/100:
                self.entity_manager.add(
                        Entity(PositionComponent = {'x':e['Position']['x'],
                                                    'y':e['Position']['y']},
                               VelocityComponent = {'x':randint(-500,500)/100,
                                                    'y':randint(-10,0)-6},
                               ParticleComponent = True,
                               TimerComponent    = {'timer':10, 'time':.4}))
            # self.entity_manager.add(
            #         Entity(PositionComponent = {'x':e['Position']['x'],
            #                                     'y':e['Position']['y']},
            #                VelocityComponent = {'x':randint(-500,500)/100,
            #                                     'y':randint(0,10)+6},
            #                ParticleComponent = True,
            #                TimerComponent    = {'timer':6, 'time':.4}))
                self.elapsed=0

# class MoveSystem:
# class RenderSystem:
