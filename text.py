import pygame
pygame.font.init()

def create_fonts(font='Arial', sizes=[16]):
    """Creates different fonts with one list"""
    fonts = []
    for size in sizes:
        fonts.append(pygame.font.SysFont(font, size))
    return fonts


def render(font, what, color, where, canvas):
    """Renders the fonts as passed from display_fps"""
    text_to_show = font.render(what, 0, pygame.Color(color))
    canvas.blit(text_to_show, where)


def display_fps(font, clock, canvas):
    """Data that will be rendered and blitted in _display"""
    render(
        font,
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0), canvas=canvas)

arial = create_fonts(sizes=list(range(64+1)))
