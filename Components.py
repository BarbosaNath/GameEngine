import pygame
class PositionComponent:
    def __init__(self, x=0, y=0):
        if isinstance(x, list) or isinstance(x,tuple):
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

class SpriteComponent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class VelocityComponent:
    def __init__(self, x=0, y=0):
        if isinstance(x, list) or isinstance(x,tuple):
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y


class TimerComponent:
    def __init__(self, timer=0):
        self.timer = timer
