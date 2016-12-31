import sys
import os


def main():
    size = 0

    try:
        for path, subdirs, files in os.walk(sys.argv[1]):
            for file in files:
                size += os.path.getsize(path + "/" + file)
        size = size * 10 ** (-9)
    except OSError as error:
        print(error)

    print("The size of {0} is: {1:.3f} GB".format(sys.argv[1], size))


if __name__ == '__main__':
    main()
