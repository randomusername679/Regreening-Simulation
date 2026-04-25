from pyglm import glm
import math

def rotate_x(pos: glm.vec3, theta):
    return glm.vec3(
        pos.x,
        pos.y * math.cos(theta) - pos.z * math.sin(theta),
        pos.y * math.sin(theta) + pos.z * math.cos(theta)
    )

def rotate_y(pos: glm.vec3, theta):
    return glm.vec3(
        pos.x * math.cos(theta) + pos.z * math.sin(theta),
        pos.y,
        pos.x * -math.sin(theta) + pos.z * math.cos(theta)
    )

def rotate_z(pos: glm.vec3, theta):
    return glm.vec3(
        pos.x * math.cos(theta) - pos.y * math.sin(theta),
        pos.x * math.sin(theta) + pos.y * math.cos(theta),
        pos.z
    )