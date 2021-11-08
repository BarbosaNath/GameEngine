# from PIL import Image
import PIL.Image, PIL.ImageFilter
import pygame
import cv2
import numpy
from DebugLog import debugLog

def Bloom(canvas: pygame.Surface):
    size = canvas.get_size()
    # canvas_zero = canvas
    canvas_color = pygame.surfarray.array2d(canvas)
    canvas_rgba = canvas_color.view(dtype=numpy.uint8).reshape((*canvas_color.shape, 4))

    newCanvas = pygame.Surface(size, pygame.SRCALPHA)
    newCanvas.set_colorkey((0,0,0))


    cv2.GaussianBlur(canvas_rgba, ksize=(9, 9), sigmaX=10, sigmaY=10, dst=canvas_rgba)
    cv2.blur(canvas_rgba, ksize=(9, 9), dst=canvas_rgba)

    # newCanvas.blit(pygame.surfarray.make_surface(canvas), (0,0))
    # new = pygame.image.frombuffer(canvas_rgba, size, 'RGBA')
    # newCanvas.blit(
    #     pygame.transform.flip(pygame.transform.rotate(new, 90),0,1),
    #     (0,0))
    pygame.surfarray.blit_array(newCanvas, canvas_color)
    # newCanvas.blit(canvas_zero, (0,0))

    return newCanvas
