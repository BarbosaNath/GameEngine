import pygame, os
from Entity import Entity
from GenericEntities import Particle
from EntityManager import EntityManager
from math import cos, sin
from random import randint
from config import config

# TODO: Better config managemant
# TODO: better particle bloom expansion
# TODO: manage the 2 bloom surfaces

# Particle System --------------------------------------------------------------
class ParticleSystem:
    def __init__(self, entity_manager, canvas, bloomLayer):
        self.entity_manager = entity_manager
        self.canvas = canvas
        self.bloomLayer = bloomLayer

    def update(self, dt):
        for id in self.entity_manager.filter(('Particle', 'Position',
                                              'Velocity', 'Timer')):
            e = self.entity_manager[id]
            pos  = (e['Position']['x'], e['Position']['y'])
            vel  = (e['Velocity']['x'], e['Velocity']['y'])
            timer = e['Timer']['timer']

            e['Position']['x'] += vel[0]*20*dt
            e['Position']['y'] += vel[1]*20*dt


            if config['bloom']:
                pygame.draw.circle(self.bloomLayer, (255,120,120), pos, timer)
            pygame.draw.circle(self.canvas, (255,255,255), pos, timer)


            e['Velocity']['x'] *= 0.99
            e['Velocity']['y'] *= 0.99

            e['Timer']['timer'] -= e['Timer']['time']*20*dt
            if timer <= 0: self.entity_manager.remove(id)


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
    def __init__(self, em):
        self.entity_manager = em
        self.elapsed = 0

    def update(self, dt):
        self.elapsed += dt

        for id in self.entity_manager.filter(('ParticleSpawner','Position')):
            e = self.entity_manager[id]
            pos = (e['Position']['x'], e['Position']['y'])
            vel = (randint(-500,500)/100, randint(-10,0)-6)

            # Particle ---------------------------------------------------------
            if self.elapsed >= config['particles']/100:
                self.entity_manager.add(Particle().setPos(pos).setVel(vel))
                self.elapsed=0

# class MoveSystem:
# class RenderSystem:
