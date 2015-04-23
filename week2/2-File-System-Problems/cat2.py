import sys


def cat2():
    text = ""

    if len(sys.argv) > 1:
        index = 1

        while index < len(sys.argv):
            filename = sys.argv[index]
            text_file = open(filename, "r")
            text += text_file.read()
            text_file.close()
            index += 1
    else:
        print("You haven't specified filenames!")

    return text


def main():
    print(cat2())

if __name__ == '__main__':
    main()
