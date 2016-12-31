import sys


def main():
    if len(sys.argv) > 1:
        filenames = sys.argv[1:]
        for filename in filenames:
            with open(filename, "r") as file:
                print(file.read())
    else:
        print("You haven't specified filenames!")


if __name__ == '__main__':
    main()
