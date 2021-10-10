# TODO: cffi
# import pymunk
import pygame
import os, sys
import random
from Components import *
from Entity import Entity
from EntityManager import EntityManager

# os.system('cls')

pygame.init()


def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts


def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_fps():
    "Data that will be rendered and blitted in _display"
    render(
        fonts[0],
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))


fonts= create_fonts([32,16,14,8])

screen = pygame.display.set_mode((500, 500),pygame.DOUBLEBUF)
clock  = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,pygame.KEYUP])

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

em = EntityManager()

seconds = 0.0

while 1:

    dt = clock.get_time()/1000.0

    seconds += dt
    if seconds > 0.02:
        em.add(Entity(( PositionComponent(pygame.mouse.get_pos()),
                        VelocityComponent(random.randint(0,20)/10 -1, -2),
                        TimerComponent   (random.randint(4,6)) )))
        seconds = 0

    screen.fill(BLACK)


    for particle in em.entities:
        c = particle.component(TimerComponent).timer
        c = (50*c,50*c,50*c)
        def a(b):
            if b > 255: b=255
            return b

        c = tuple(map(a, c))

        particle.component(PositionComponent).x += particle.component(VelocityComponent).x*dt*20
        particle.component(PositionComponent).y += particle.component(VelocityComponent).y*dt*20
        particle.component(TimerComponent).timer -= .1*dt*20
        pygame.draw.circle( screen, c,
                            (   particle.component(PositionComponent).x,
                                particle.component(PositionComponent).y),
                            particle.component(TimerComponent).timer)
        if particle.component(TimerComponent).timer <= 0:
            em.remove(particle)



    render(fonts[0], str(len(em.entities)), 'white', (250,0))
    display_fps()


    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(2000)
