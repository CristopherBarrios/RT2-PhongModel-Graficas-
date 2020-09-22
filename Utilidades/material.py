# Cristopher Jose Rodolfo Barrios Solis 18207
# RT2

from Utilidades.utils import Color
from Utilidades.math import V3

WHITE = Color(255, 255, 255)


class Light(object):
    def __init__(self, position=V3(0, 0, 0), intensity=1):
        self.position = position
        self.intensity = intensity


class Material(object):
    def __init__(self, diffuse=WHITE, albedo=(1, 0), spec=0):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec


class Intersect(object):
    def __init__(self, distance, point, normal):
        self.distance = distance
        self.point = point
        self.normal = normal
