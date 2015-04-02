import math


def tetrahedron_filled(tetrahedrons, water):
    tetrahedrons.sort()
    filled_tetrahedrons = 0
    for tetrahedron in tetrahedrons:
        volume = math.sqrt(2) * (tetrahedron ** 3) / 12
        volume = volume / 1000
        if water >= volume:
            filled_tetrahedrons += 1
        water = water - volume
    print(filled_tetrahedrons)

# Examples
tetrahedron_filled([100, 20, 30], 10)
tetrahedron_filled([50, 20, 30], 30)
