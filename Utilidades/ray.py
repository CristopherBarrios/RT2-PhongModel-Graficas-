# Cristopher Jose Rodolfo Barrios Solis 18207
# RT2

from Utilidades.utils import *
from Utilidades.sphere import Sphere
from Utilidades.math import norm, V3, dot, mul, sum, reflect, sub, length
from math import tan, pi

GREY = Color(54, 69, 79)


class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = GREY
        self.scene = []
        self.light = None
        self.clear()

    def clear(self):
        self.pixels = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename):
        writebmp(filename, self.width, self.height, self.pixels)

    def finish(self, filename="final.bmp"):
        self.render()
        self.write(filename)

    def point(self, x, y, c=None):
        try:
            self.pixels[y][x] = c or self.current_color
        except:
            pass

    def scene_intersect(self, orig, direction):
        zbuffer = float("inf")

        material = None
        intersect = None

        for obj in self.scene:
            hit = obj.ray_intersect(orig, direction)
            if hit is not None:
                if hit.distance < zbuffer:
                    zbuffer = hit.distance
                    material = obj.material
                    intersect = hit

        return material, intersect

    def cast_ray(self, orig, direction):
        material, intersect = self.scene_intersect(orig, direction)

        if material is None:
            return self.background_color

        light_dir = norm(sub(self.light.position, intersect.point))
        light_distance = length(sub(self.light.position, intersect.point))

        offset_normal = mul(intersect.normal, 1.1) 
        shadow_orig = (
            sub(intersect.point, offset_normal)
            if dot(light_dir, intersect.normal) < 0
            else sum(intersect.point, offset_normal)
        )
        shadow_material, shadow_intersect = self.scene_intersect(shadow_orig, light_dir)
        shadow_intensity = 0

        if (
            shadow_material
            and length(sub(shadow_intersect.point, shadow_orig)) < light_distance
        ):
            shadow_intensity = 0.9

        intensity = (
            self.light.intensity
            * max(0, dot(light_dir, intersect.normal))
            * (1 - shadow_intensity)
        )

        reflection = reflect(light_dir, intersect.normal)
        specular_intensity = self.light.intensity * (
            max(0, -dot(reflection, direction)) ** material.spec
        )

        diffuse = material.diffuse * intensity * material.albedo[0]
        specular = Color(255, 255, 255) * specular_intensity * material.albedo[1]
        return diffuse + specular

    def render(self):
        print("Compilando...")
        fov = int(pi / 2)
        for y in range(self.height):
            for x in range(self.width):
                i = (
                    (2 * (x + 0.5) / self.width - 1)
                    * tan(fov / 2)
                    * self.width
                    / self.height
                )
                j = (2 * (y + 0.5) / self.height - 1) * tan(fov / 2)
                direction = norm(V3(i, j, -1))
                self.pixels[y][x] = self.cast_ray(V3(0, 0, 0), direction)
