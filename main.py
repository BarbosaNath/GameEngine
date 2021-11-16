import pygame, sys, os
from random        import randint
from Entity        import Entity
from EntityManager import EntityManager
from Systems       import *
from World         import World
from text          import create_fonts, render, display_fps
from DebugLog      import debugLog, log_vars
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
GREY13  = (85,85,85)
GREY23  = (85*2,85*2,85*2)
acc     = '$#A3F$'
white   = '$#FFF$'

# Initialize pygame ------------------------------------------------------------
pygame.init()
os.system('cls')

# Initialize Pygame Variables --------------------------------------------------
screen_size = (500,500)
screen      = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF)
particleLayer  = pygame.Surface(screen_size, pygame.SRCALPHA)
bloomLayer      = pygame.Surface(screen_size, pygame.SRCALPHA)
clock       = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,pygame.KEYUP])


debugLog.add_line('', fixed=True, id='fps')


def resizeBloom(canvas, size, amount=1):
    return Bloom( pygame.transform.smoothscale(canvas, (size[0]//amount, size[1]//amount)) )
def resize(canvas, size, amount=1):
    return pygame.transform.smoothscale(canvas, (size[0]//amount, size[1]//amount))



# Initialize Entity Component System -------------------------------------------
em    = EntityManager()
world = World()
if config['particles'] != False:
    world['ParticleSystem'] = ParticleSystem(em, particleLayer, bloomLayer)
    world['ParticleSpawnerSystem'] = ParticleSpawnerSystem(em)

# Player -----------------------------------------------------------------------
em.add(Entity(Controller = {},
              Sprite     = 'player.png',
              Position   = {'x':0,'y':0},
              Velocity   = {'x':0,'y':0},
              Direction  = {'x':0,'y':0}))

em.add(Entity(ParticleSpawner = { 'range'   : [0,100],
                                  'arc'     : [0,360],
                                  'rotation': [0,360],
                                  'scale'   :      5},
              Position = {'x':0,'y':0}))

# Begin main game loop ---------------------------------------------------------
frames=0
world.update(10)
while 1:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
          (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()


    # Mouse variable for easy access -------------------------------------------
    mouse = pygame.mouse.get_pos()
    em['1']['Position']['x'] = mouse[0] # Update particle spawner position
    em['1']['Position']['y'] = mouse[1] # Update particle spawner position

    # Delta Time variable ------------------------------------------------------
    dt = clock.get_time()/1000.0

    # Reset screens ------------------------------------------------------------
    screen.fill(BLACK)
    particleLayer.fill((0,0,0,0))
    bloomLayer.fill((0,0,0,0))

    # Update every system ------------------------------------------------------
    world.update(dt)

    # Draw Particles and Bloom -------------------------------------------------
    if config['bloom']:
        if frames%config['bloom_rate'] == 0:
            size = bloomLayer.get_size()
            bloomSurface = pygame.Surface(size, pygame.SRCALPHA)
            if config['bloom_depth'] >= 2: bloomSurface.blit(resize(resizeBloom(bloomLayer, size, 2), size),(0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
            if config['bloom_depth'] >= 3: bloomSurface.blit(resize(resizeBloom(bloomSurface, size, 4), size),(0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
            bloomSurface.blit(Bloom(bloomLayer), (0,0), special_flags=pygame.BLEND_RGBA_ADD)
            bloomSurface.blit(Bloom(bloomSurface), (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
            del size
        screen.blit(bloomSurface, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
    screen.blit(particleLayer, (0,0))

    # Render the debugLog ------------------------------------------------------
    if config['debug']:
        debugLog.edit_line('fps', 'text', log_vars('FPS', int(clock.get_fps()), 'Entities', len(em)))
        if frames%config['debug_delay']==0: debugLog.render()
        screen.blit(debugLog.canvas, (0,0))

    # Update and tick screen ---------------------------------------------------
    pygame.display.update()
    clock.tick(config['fps'])

    frames+=1
