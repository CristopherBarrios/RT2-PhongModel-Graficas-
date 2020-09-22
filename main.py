from Utilidades.ray import Raytracer, GREY
from Utilidades.material import Material, Light
from Utilidades.sphere import Sphere
from Utilidades.utils import Color
from Utilidades.math import V3

## Colorsitos
cafe = Color(200, 94, 38)
cafeClaro = Color(245, 180, 150)
blanquito = Color(248, 248, 248)
verde = Color(154, 255, 52)
rojo = Color(255, 52, 52)
gris = Color(200, 200, 200)
negro = Color(40, 40, 40)


Cafecafe = Material(diffuse=cafe, albedo=(0.92, 0.92), spec=30)
chocolate = Material(diffuse=cafeClaro, albedo=(0.92, 0.82), spec=30)
musgo = Material(diffuse=verde, albedo=(0.64, 0.36), spec=15)
ROjo = Material(diffuse=rojo, albedo=(0.64, 0.36), spec=15)
hierro = Material(diffuse=gris, albedo=(1, 1), spec=30)
ojo = Material(diffuse=negro, albedo=(0.64, 0.36), spec=5)
cuerpo1 = Material(diffuse=blanquito, albedo=(0.86, 0.86), spec=30)


rndr = Raytracer(800, 800)
rndr.light = Light(position=V3(4, 0.5, 20), intensity=1.5)
rndr.background_color = blanquito



rndr.scene = [
    ################### Oso Izquierda

        # cabeza
    Sphere(V3(-2.5, 1.7, -10), 1.25, cuerpo1),
    Sphere(V3(-2.5, 1.7, -9.2), 0.4, cuerpo1),
    Sphere(V3(-3.4, 2.74, -9.5), 0.4, cuerpo1),
    Sphere(V3(-1.5, 2.74, -9.5), 0.4, cuerpo1),
    Sphere(V3(-2.5, 1.7, -9), 0.1, ojo),
    Sphere(V3(-2.6, 2.3, -9), 0.1, ojo),
    Sphere(V3(-2, 2.3, -9), 0.1, ojo),

        # moño
    Sphere(V3(-2.6, 0.1, -9.2), 0.20, ROjo),

    # Cuerpo
    Sphere(V3(-2.5, -1, -10), 1.5, hierro),
    Sphere(V3(-3.94, -0.2, -10), 0.6, cuerpo1),
    Sphere(V3(-3.94, -2.2, -10), 0.6, cuerpo1),
    Sphere(V3(-1.09, -0.2, -10), 0.6, cuerpo1),
    Sphere(V3(-1.09, -2.2, -10), 0.6, cuerpo1),

    ######################## oso derecha
        # cabeza
    Sphere(V3(2.5, 1.7, -10), 1.25, chocolate),
    Sphere(V3(2.5, 1.7, -9.2), 0.4, Cafecafe),
    Sphere(V3(3.4, 2.74, -9.5), 0.4, Cafecafe),
    Sphere(V3(1.5, 2.74, -9.5), 0.4, Cafecafe),
    Sphere(V3(2.5, 1.7, -9), 0.1, ojo),
    Sphere(V3(2.6, 2.3, -9), 0.1, ojo),
    Sphere(V3(2, 2.3, -9), 0.1, ojo),

        # moño
    Sphere(V3(2.6, 0.1, -9.2), 0.20, musgo),

        # cuerpo
    Sphere(V3(2.5, -1, -10), 1.5, ROjo),
    Sphere(V3(3.94, -0.2, -10), 0.6, chocolate),
    Sphere(V3(3.94, -2.2, -10), 0.6, chocolate),
    Sphere(V3(1.09, -0.2, -10), 0.6, chocolate),
    Sphere(V3(1.09, -2.2, -10), 0.6, chocolate),

]

rndr.finish()
