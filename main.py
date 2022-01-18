import pygame, sys, os, json
from random        import randint
from Entity        import Entity
from EntityManager import EntityManager
from Systems       import *
from World         import World
from DebugLog      import debugLog, log_vars
from postProcessing import Bloom
from config import config
from debugUI import DebugUI
import config as Config
from utils  import resizeBloom

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
particleLayer = pygame.Surface(screen_size, pygame.SRCALPHA)
bloomLayer    = pygame.Surface(screen_size, pygame.SRCALPHA)
clock = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,pygame.KEYUP])


debugLog.add_line('', fixed=True, id='fps')


debugUI = DebugUI(screen,(300, 50),(200,250))
debugUI.add('fps_label', label='FPS')
debugUI.add('fps',   label='FPS', type='scroll', action=lambda x: Config.reload('fps', x), rnge=[0,600], module=60, bignumbers=True)
debugUI.add('bloom', label='Bloom', type='checkbox', action=lambda x: Config.reload('bloom', x))
debugUI.add('bloom_rate_label', label='Bloom Rate')
debugUI.add('bloom_rate', label='Bloom Rate', type='scroll', action=lambda x: Config.reload('bloom_rate', x), rnge=[1,5])
debugUI.add('bloom_depth_label', label='Bloom Depth')
debugUI.add('bloom_depth', label='Bloom Depth', type='scroll', action=lambda x: Config.reload('bloom_depth', x), rnge=[1,3])
debugUI.add('particles_label', label='Particles')
debugUI.add('Particles', label='Particles', type='scroll', action=lambda x: Config.reload('particles', x), rnge=[0,5])
debugUI.add('load', label='load', type='button')

# Initialize Entity Component System -------------------------------------------
em    = EntityManager()
world = World()
if config['particles'] != False:
    world['ParticleSystem'] = ParticleSystem(em, particleLayer, bloomLayer)
    world['ParticleSpawnerSystem'] = ParticleSpawnerSystem(em)

# Player -----------------------------------------------------------------------
em.addID('Player',
       Entity(Controller = {},
              Sprite     = 'player.png',
              Position   = {'x':0,'y':0},
              Velocity   = {'x':0,'y':0},
              Direction  = {'x':0,'y':0}))

# Particle Spawner -------------------------------------------------------------
em.addID('ParticleSpawner',
        {'ParticleSpawner': {'range'   : [0,100],
                             'arc'     : [0,360],
                             'rotation': [0,360],
                             'scale'   :      5},
          'Position': {'x':250,'y':250}})


# Begin main game loop ---------------------------------------------------------
frames=0
world.update(10)
while 1:
    # Keypress handler ---------------------------------------------------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
          (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()


    # Mouse variable for easy access -------------------------------------------
    mouse = pygame.mouse.get_pos()
    em['ParticleSpawner']['Position']['x'] = mouse[0] # Update particle spawner position
    em['ParticleSpawner']['Position']['y'] = mouse[1] # Update particle spawner position


    # Delta Time variable ------------------------------------------------------
    dt = clock.get_time()/1000.0


    # Reset screens ------------------------------------------------------------
    screen.fill(BLACK)
    particleLayer.fill((0,0,0,0))
    bloomLayer.fill((0,0,0,0))


    # Update every system ------------------------------------------------------
    world.update(dt)


    # Draws Bloom --------------------------------------------------------------
    if config['bloom']:
        # Only draws the bloom on some frames ----------------------------------
        if frames%config['bloom_rate'] == 0:
            size = bloomLayer.get_size()
            bloomSurface = pygame.Surface(size, pygame.SRCALPHA)
            # 2nd Pass of bloom ------------------------------------------------
            if config['bloom_depth'] >= 2: bloomSurface.blit(resizeBloom(bloomLayer  , size, 2),(0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
            # 3rd Pass of bloom ------------------------------------------------
            if config['bloom_depth'] >= 3: bloomSurface.blit(resizeBloom(bloomSurface, size, 4),(0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
            # 1st Pass of bloom ------------------------------------------------
            bloomSurface.blit(Bloom(bloomLayer  ), (0,0), special_flags=pygame.BLEND_RGBA_ADD)
            bloomSurface.blit(Bloom(bloomSurface), (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
            del size
        screen.blit(bloomSurface, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)


    # Draws Particles ----------------------------------------------------------
    screen.blit(particleLayer, (0,0))
# TODO: add config to systems.update(dt,config)

    # Render the debugLog ------------------------------------------------------
    if config['debug']:
        debugLog.edit_line('fps', 'text', log_vars('FPS', int(clock.get_fps()), 'Entities', len(em)))
        if frames%config['debug_delay']==0: debugLog.render()
        debugUI.render()
        screen.blit(debugLog.canvas, (0,0))

    # print(config)
    # if debugUI['load']['just_pressed']:
    with open('config.json', 'r') as file:
        config = json.load(file)


    # Update and tick screen ---------------------------------------------------
    frames+=1
    pygame.display.update()
    clock.tick(config['fps'])
