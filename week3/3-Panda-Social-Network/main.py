from panda_social_network import Panda
from panda_social_network import PandaSocialNetwork


def main():
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    print(ivo.get_name() == "Ivo")  # True
    print(ivo.get_email() == "ivo@pandamail.com")  # True
    print(ivo.get_gender() == "male")  # True
    print(ivo.isMale() == True)  # True
    print(ivo.isFemale() == False)  # True

    network = PandaSocialNetwork()

    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "female")

    for panda in [ivo, rado, tony]:
        network.add_panda(panda)

    network.make_friends(ivo, rado)
    network.make_friends(rado, tony)

    print(network.connection_level(ivo, rado) == 1)  # True
    print(network.connection_level(ivo, tony) == 2)  # True

    print(network.how_many_gender_in_network(1, rado, "female"))   # True

    network.save_social_network("save_network.txt")
    network.load_social_network("save_network.txt")
    network.save_social_network("load_network.txt")

if __name__ == '__main__':
    main()
