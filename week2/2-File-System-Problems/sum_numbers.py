import sys


def main():
    filename = sys.argv[1]
    text_file = open(filename, "r")
    content = text_file.read().split(" ")
    content = [int(x) for x in content]
    text_file.close()

    return(sum(content))

if __name__ == '__main__':
    print(main())
