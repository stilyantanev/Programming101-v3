from music_player import MusicPlayer


def main():
    try:
        player = MusicPlayer()

        print("Welcome! I am the Music Player!")
        print("Have fun!")
        print("Type list to see all possible commands!")

        while True:
            command = input("Enter command:")
            command = command.lower()

            if command == "list":
                print("All possible commands:")
                print("add")
                print("stop")
                print("next")
                print("previous")
                print("repeat")
                print("shuffle")
                print("show")
                print("quit")
            elif command == "add":
                directory = input("Please enter directory:")
                player.add_songs(directory)
                print("Songs was added!")
            elif command == "stop":
                player.stop_playing()
            elif command == "next":
                player.stop_playing()
                player.play_next(directory)
            elif command == "previous":
                player.stop_playing()
                player.play_previous(directory)
            elif command == "repeat":
                mode = input("Enter repeat mode (True or False):")
                player.change_repeat_mode(mode)
            elif command == "shuffle":
                mode = input("Enter shuffle mode (True or False):")
                player.change_shuffle_mode(mode)
            elif command == "show":
                player.show_playlist()
            elif command == "quit":
                print("Bye!")
                break
            else:
                print("Try command from the list!")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
