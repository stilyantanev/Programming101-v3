import sys


def main():
    if len(sys.argv) > 1:
        index = 1
        text = ""
        while index < len(sys.argv):
            filename = sys.argv[index]
            text_file = open(filename, "r")
            text += text_file.read()
            text_file.close()
            index += 1
        return text
    else:
        print("You haven't specified filenames!")

if __name__ == '__main__':
    print(main())
