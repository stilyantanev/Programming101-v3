import math


def fill_tetrahedron(num):
    volume = math.sqrt(2) * (num ** 3) / 12
    volume = volume / 1000
    print("{0:.2f}".format(volume))

# Examples
fill_tetrahedron(100)
fill_tetrahedron(200)
