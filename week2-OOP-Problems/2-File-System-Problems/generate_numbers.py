import sys
from random import randint


def main():
    filename = sys.argv[1]
    numbers = int(sys.argv[2])
    with open(filename, "w") as file:
        for number in range(0, numbers):
            file.write(str(randint(1, 1000)) + " ")


if __name__ == '__main__':
    main()
