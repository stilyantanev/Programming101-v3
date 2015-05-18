from settings import DATABASE
from controller import Controller
from view import View


def main():
    controller = Controller(DATABASE)
    view = View(controller)

    view.start_taking_commands()

if __name__ == '__main__':
    main()
