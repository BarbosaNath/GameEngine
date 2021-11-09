# from PIL import Image
import PIL.Image, PIL.ImageFilter
import pygame
import cv2
import numpy
from DebugLog import debugLog
from config import config


def Bloom(canvas: pygame.Surface):
    KSIZE = (9,9)
    SIGMA = 20

    size = canvas.get_size()
    canvas_color = pygame.surfarray.array2d(canvas)
    canvas_rgba = canvas_color.view(dtype=numpy.uint8).reshape((*canvas_color.shape, 4))

    newCanvas = pygame.Surface(size, pygame.SRCALPHA)
    newCanvas.set_colorkey((0,0,0))

    cv2.GaussianBlur(canvas_rgba, ksize=KSIZE, sigmaX=SIGMA, sigmaY=SIGMA, dst=canvas_rgba)
    cv2.blur(canvas_rgba, ksize=(9, 9), dst=canvas_rgba)
    pygame.surfarray.blit_array(newCanvas, canvas_color)


    return newCanvas
