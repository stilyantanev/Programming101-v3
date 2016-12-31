import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, "r") as file:
            print(file.read())
    else:
        print("You haven't specified filename!")


if __name__ == '__main__':
    main()
