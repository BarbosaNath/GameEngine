from Entity import Entity

# class Spawner(Entity):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#         self['Spawner'] = {'Velocity':[]}
#         self['Entity' ] = Particle()
#         # self[''] =
#
#
class Particle(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self['Particle'] = True
        self['Position'] = {'x':0,'y':0}
        self['Velocity'] = {'x':0,'y':0}
        self['Timer']    = {'timer':10, 'time':.4}

    def setVel(self, vel):
        self['Velocity']['x'] = vel[0]
        self['Velocity']['y'] = vel[1]
        return self
    def setPos(self, pos):
        self['Position']['x'] = pos[0]
        self['Position']['y'] = pos[1]
        return self
    def setTimer(self, timer: float, time: float):
        self['Timer']['timer'] = timer
        self['Timer']['time' ] = time
        return self
