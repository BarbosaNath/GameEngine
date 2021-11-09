import pygame, sys, os
from random        import randint
from Entity        import Entity
from EntityManager import EntityManager
from Systems       import *
from World         import World
from text          import create_fonts, render, display_fps
from DebugLog      import debugLog
from postProcessing import Bloom
from PIL import Image, ImageShow
from config import config

# Simple color access ----------------------------------------------------------
WHITE   = 0xffffff
CYAN    = 0x00ffff
BLUE    = 0x0000ff
MAGENTA = 0xff00FF
RED     = 0xff0000
YELLOW  = 0xffff00
BLACK   = 0x000000
GREY    = (50,50,50)
acc     = '$#A3F$'
white   = '$#FFF$'




# Initialize pygame ------------------------------------------------------------
pygame.init()
os.system('cls')

# Initialize Pygame Variables --------------------------------------------------
screen_size = (500,500)


screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF)
bloomLayer = pygame.Surface(screen_size, pygame.SRCALPHA)
layer2 = pygame.Surface(screen_size, pygame.SRCALPHA)
clock  = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,pygame.KEYUP])


debugLog.add_line(f'{acc}FPS{acc}: {int(clock.get_fps())}', fixed=True, id='fps')


# Initialize Entity Component System -------------------------------------------
em    = EntityManager()
world = World()
if config['particles'] != False:
    world['ParticleSpawnerSystem'] = ParticleSpawnerSystem(em)
    world['ParticleSystem'       ] = ParticleSystem(em, bloomLayer, layer2)

# Player -----------------------------------------------------------------------
em.add(Entity(ControllerComponent = {},
              SpriteComponent     = 'player.png',
              PositionComponent   = {'x':0,'y':0},
              VelocityComponent   = {'x':0,'y':0},
              DirectionComponent  = {'x':0,'y':0},
             ) )

em.add(Entity(ParticleSpawner = { 'range'   : [0,100],
                                  'arc'     : [0,360],
                                  'rotation': [0,360],
                                  'scale'   :      5},
              Position        = {'x':250,'y':250},
))

# bloomSurface = bloomLayer
# Begin main game loop ---------------------------------------------------------
even=0
world.update(10)
while 1:
    fpsText = f'{acc}FPS{white}: {int(clock.get_fps())}   $#3AF$|{acc}   Entities{white}: {len(em)}'

    # Mouse variable for easy access -------------------------------------------
    # mouse = pygame.mouse.get_pos()

    # Delta Time variable ------------------------------------------------------
    dt = clock.get_time()/1000.0

    # Reset screens ------------------------------------------------------------
    screen.fill(GREY)
    # if even%2 != 0:
    bloomLayer.fill((0, 0, 0, 0))
    layer2.fill((0,0,0,0))

    # Update every system ------------------------------------------------------
    world.update(dt)

    # Handle pygame events -----------------------------------------------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
          (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()


    debugLog.edit_line('fps', 'text', fpsText)
    debugLog.render()
    screen.blit(debugLog.canvas, (0,0))
    if config['bloom']:
        if even%config['bloom_rate'] == 0:
            bloomSurface = Bloom(layer2)
            # bloomSurface2 = Bloom(bloomLayer)
        # screen.blit(layer2, (0,0))
        screen.blit(bloomSurface, (0,0))
    screen.blit(bloomLayer, (0,0))

    # Update and tick screen ---------------------------------------------------
    pygame.display.update()
    clock.tick(config['fps'])

    even+=1
