import sys
import os


def main():
    size = 0

    for path, subdirs, files in os.walk(sys.argv[1]):
        for file in files:
            every_file = path + "/" + file
            size += os.path.getsize(every_file)

    size = size * 10 ** (-9)

    return size

if __name__ == '__main__':
    print("The size of {0} is: {1} GB".format(sys.argv[1], main()))
