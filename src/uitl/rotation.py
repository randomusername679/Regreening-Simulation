import math
import pygame

# the theta in all of these functions should be in radians
def rotate_x(pos: pygame.math.Vector3, theta):
    return pygame.math.Vector3(pos.x, math.cos(theta) * pos.y - math.sin(theta) * pos.z, math.sin(theta) * pos.y + math.cos(theta) * pos.z)

def rotate_y(pos: pygame.math.Vector3, theta):
    return pygame.math.Vector3(math.cos(theta) * pos.x - math.sin(theta) * pos.z, pos.y, math.sin(theta) * pos.x + math.cos(theta) * pos.z)

def rotate_z(pos: pygame.math.Vector3, theta):
    return pygame.math.Vector3(math.cos(theta) * pos.x - math.sin(theta) * pos.y, math.sin(theta) * pos.x + math.cos(theta) * pos.y, pos.z)
