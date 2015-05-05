from social_network import Network
from user import User
from pprint import pprint


def main():
    stilyan = User("stilyantanev")
    filip = User("lucifer666")
    rado = User("RadoRado")

    filip_net = Network()
    filip_net.build_social_graph(1, filip)
    pprint(filip_net.graph.nodes)

    print()

    stilyan_net = Network()
    stilyan_net.build_social_graph(1, stilyan)
    pprint(stilyan_net.graph.nodes)

    print()

    print(filip_net.do_you_follow(stilyan))
    print(filip_net.do_you_follow_indirectly(stilyan))
    print(filip_net.does_he_she_follows(stilyan))
    print(filip_net.do_you_follow_indirectly(stilyan))
    print(filip_net.who_follows_you_back())

    print()

    print(stilyan_net.do_you_follow(rado))
    print(stilyan_net.do_you_follow_indirectly(rado))
    print(stilyan_net.does_he_she_follows(rado))
    print(stilyan_net.do_you_follow_indirectly(rado))
    print(stilyan_net.who_follows_you_back())

if __name__ == '__main__':
    main()
