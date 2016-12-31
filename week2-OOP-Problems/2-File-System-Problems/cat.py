import sys


def cat():
    text = ""

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text_file = open(filename, "r")
        text = text_file.read()
        text_file.close()
    else:
        print("You haven't specified filename!")

    return text


def main():
    print(cat())

if __name__ == '__main__':
    main()
