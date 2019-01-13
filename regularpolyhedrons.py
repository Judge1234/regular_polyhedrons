from math import sqrt




#   Tetrahedron
def tetrahedron_volume(l):
    v = (l**3) / (6 * sqrt(2))
    return v


def tetrahedron_surface_area(l):
    a = sqrt(3) * (l**2)
    return a


#   Cube
def cube_volume(l):
    v = l**3
    return v


def cube_surface_area(l):
    a = 6 * (l**2)
    return a


#   Octahedron
def octahedron_volume(l):
    v = (sqrt(2) / 3) * (l**3)
    return v


def octahedron_surface_area(l):
    a = (2 * sqrt(3)) * (l**2)
    return a


#   Dodecahedron
def dodecahedron_volume(l):
    t = 15 + (7 * sqrt(5))
    v = (t / 4) * (l**3)
    return v


def dodecahedron_surface_area(l):
    i = 25 + (10 * sqrt(5))
    a = (3 * sqrt(i)) * (l**2)
    return a


#   Icosahedron
def icosahedron_volume(l):
    t = 5 * (3 + sqrt(5))
    v = (t / 12) * (l**3)
    return v


def icosahedron_surface_area(l):
    a = (5 * sqrt(3)) * (l**2)
    return a








