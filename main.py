import pygame, sys, os
from random        import randint
from Entity        import Entity
from EntityManager import EntityManager
from Systems       import ControlSystem, ParticleSystem
from World         import World
from text          import create_fonts, render, display_fps
from DebugLog      import debugLog


# Simple color access ----------------------------------------------------------
WHITE   = (255,255,255)
CYAN    = (  0,255,255)
BLUE    = (  0,  0,255)
MAGENTA = (255,  0,255)
RED     = (255,  0,  0)
YELLOW  = (255,255,  0)
BLACK   = (  0,  0,  0)


# Initialize pygame ------------------------------------------------------------
pygame.init()
os.system('cls')

# Initialize Pygame Variables --------------------------------------------------
screen = pygame.display.set_mode((500, 500),pygame.DOUBLEBUF)
clock  = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,pygame.KEYUP])

debugLog.add_line(f'fps: {int(clock.get_fps())}')
debugLog.add_line(f'Teste')

# Available ID Generator -------------------------------------------------------
# id = '-1'
# def next_id():
#     global id
#     id = str(int(id)+1)
#     return id


# Initialize Entity Component System -------------------------------------------
# em    = EntityManager()
# world = World(ControlSystem  = ControlSystem (em),
#               ParticleSystem = ParticleSystem(em, screen))

# Player -----------------------------------------------------------------------
# em[next_id()] = Entity(ControllerComponent = {},
#                        SpriteComponent     = 'player.png',
#                        PositionComponent   = {'x':0,'y':0},
#                        VelocityComponent   = {'x':0,'y':0},
#                        DirectionComponent  = {'x':0,'y':0},
#                       )

# Begin main game loop ---------------------------------------------------------
while 1:
    # Mouse variable for easy access -------------------------------------------
    # mouse = pygame.mouse.get_pos()

    # Delta Time variable ------------------------------------------------------
    dt = clock.get_time()/1000.0

    # Reset screen -------------------------------------------------------------
    screen.fill(BLACK)

    # Update every system ------------------------------------------------------
    # world.update(dt)

    # Handle pygame events -----------------------------------------------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
          (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()


    debugLog.edit_line(0,'text',f'FPS: {int(clock.get_fps())}')
    debugLog.render(screen,(0,0))

    # Update and tick screen ---------------------------------------------------
    pygame.display.update()
    clock.tick(60)




















    # Particle -----------------------------------------------------------------
    # em[next_id()]=Entity(PositionComponent = {'x':250,'y':250},
    #                      VelocityComponent = {'x':randint(-36,36),'y':randint(-36,36)},
    #                      ParticleComponent = True,
    #                      TimerComponent    = {'timer':3, 'time':.4})
