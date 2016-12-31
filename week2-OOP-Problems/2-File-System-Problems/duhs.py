import sys
import os


def duhs():
    size = 0

    try:
        for path, subdirs, files in os.walk(sys.argv[1]):
            for file in files:
                every_file = path + "/" + file
                size += os.path.getsize(every_file)
        size = size * 10 ** (-9)
    except OSError as error:
        print(error)

    return size


def main():
    print("The size of {0} is: {1} GB".format(sys.argv[1], duhs()))

if __name__ == '__main__':
    main()
