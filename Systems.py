import pygame
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
                pygame.draw.circle(self.canvas, (255,255,255),
                                    (entity['PositionComponent']['x'],
                                     entity['PositionComponent']['y']),
                                 entity['TimerComponent']['timer'])

                entity['VelocityComponent']['x'] *= 0.99
                entity['VelocityComponent']['y'] *= 0.99

                entity['TimerComponent']['timer']-=entity['TimerComponent']['time']*dt*20
                if entity['TimerComponent']['timer'] <= 0:
                    del self.entity_manager[i]
