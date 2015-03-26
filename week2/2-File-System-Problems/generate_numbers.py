import sys
from random import randint


def main():
    filename = sys.argv[1]
    number = int(sys.argv[2])
    random_numbers = []

    while number > 0:
        current_number = randint(1, 1000)
        random_numbers.append(str(current_number))
        number = number - 1

    text_file = open(filename, "w")
    text_file.write(" ".join(random_numbers))
    text_file.close()

if __name__ == '__main__':
    main()
