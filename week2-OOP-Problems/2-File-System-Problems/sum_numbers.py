import sys


def sum_numbers():
    filename = sys.argv[1]
    text_file = open(filename, "r")
    content = text_file.read().split(" ")
    content = [int(x) for x in content]
    text_file.close()

    return(sum(content))


def main():
    print(sum_numbers())

if __name__ == '__main__':
    main()
