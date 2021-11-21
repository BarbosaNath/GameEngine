import pygame
from postProcessing import Bloom
def hex(simplehex): # simplehex == '#FFF'
    if isinstance(simplehex, str):
        simplehex = list(simplehex)
        frst = simplehex[1]
        scnd = simplehex[2]
        thrd = simplehex[3]
        return f'#{frst}{frst}{scnd}{scnd}{thrd}{thrd}'
    else: return '#FFFFFF'



def shrink(canvas, size, amount=1):
    """Shrinks the $canvas by the $amount"""
    return pygame.transform.smoothscale(canvas, (size[0]//amount, size[1]//amount))

def shrinkBloom(canvas, size, amount=1):
    """Shrinks the $canvas by the $amount then blooms the $canvas"""
    return Bloom(pygame.transform.smoothscale(canvas, (size[0]//amount, size[1]//amount)))

def resizeBloom(canvas, size, amount=1):
    """Shrinks the $canvas' $size by the $amount,
       blooms the $canvas then
       resizes to the original $size"""
    return pygame.transform.smoothscale(Bloom(pygame.transform.scale(canvas, (size[0]//amount, size[1]//amount))), size)
