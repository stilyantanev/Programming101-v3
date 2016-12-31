import sys


def main():
    filename = sys.argv[1]
    with open(filename, "r") as file:
        numbers = file.read().strip().split(" ")
        print(sum([int(number) for number in numbers]))


if __name__ == '__main__':
    main()
