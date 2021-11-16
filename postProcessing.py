import pygame
import cv2, sys
import numpy as np

def Bloom(canvas: pygame.Surface):
    size = canvas.get_size()
    canvas_color = pygame.surfarray.array2d(canvas)
    canvas_rgba = canvas_color.view(dtype=np.uint8).reshape((*canvas_color.shape, 4))

    newCanvas = pygame.Surface(size, pygame.SRCALPHA)

    # cv2.GaussianBlur(canvas_rgba, ksize=KSIZE, sigmaX=SIGMA, sigmaY=SIGMA, dst=canvas_rgba)
    cv2.blur(canvas_rgba, ksize=(9, 9), dst=canvas_rgba)

    pygame.surfarray.blit_array(newCanvas, canvas_color)

    return newCanvas

# def ChromaKey():
