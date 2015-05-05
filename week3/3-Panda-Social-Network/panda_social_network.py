from panda_exceptions import PandaEmailException
from panda_exceptions import PandaAlreadyThereException
from panda_exceptions import PandasAlreadyFriendsException
import re
import json


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        if self.is_email_valid(email):
            self.email = email
        else:
            raise PandaEmailException
        self.gender = gender

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def is_male(self):
        return self.gender.lower() == "male"

    def is_female(self):
        return self.gender.lower() == "female"

    def __str__(self):
        message = "I am {} panda, my name is {}, for contacts: {}"

        return message.format(self.gender, self.name, self.email)

    def __repr__(self):
        message = "Panda('{}', '{}', '{}')"

        return message.format(self.name, self.email, self.gender)

    def __eq__(self, other):
        equal_names = self.name == other.name
        equal_emails = self.email == other.email
        equal_genders = self.gender == other.gender

        return equal_names and equal_emails and equal_genders

    def __hash__(self):
        return hash(self.name + self.email + self.gender)

    def is_email_valid(self, email):
        return re.search(r"[^@]+@[^@]+\.[^@]+", email)


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = {}

    def add_panda(self, panda):
        if panda in self.pandas:
            raise PandaAlreadyThereException
        else:
            self.pandas[panda] = []

    def has_panda(self, panda):
        return panda in self.pandas

    def make_friends(self, panda1, panda2):
        if panda1 not in self.pandas:
            self.pandas[panda1] = []

        if panda2 not in self.pandas:
            self.pandas[panda2] = []

        if panda1 not in self.pandas[panda2]:
            self.pandas[panda2] += [panda1]
        else:
            raise PandasAlreadyFriendsException

        if panda2 not in self.pandas[panda1]:
            self.pandas[panda1] += [panda2]
        else:
            raise PandasAlreadyFriendsException

    def are_friends(self, panda1, panda2):
        panda1_to_panda2 = panda1 in self.pandas[panda2]
        panda2_to_panda1 = panda2 in self.pandas[panda1]

        return panda1_to_panda2 and panda2_to_panda1

    def friends_of(self, panda):
        if panda not in self.pandas:
            return False
        else:
            return self.pandas[panda]

    def connection_level(self, panda1, panda2):
        visited = set()
        queue = []
        path_to = {}

        queue.append(panda1)
        visited.add(panda1)
        path_to[panda1] = None
        found = False
        path_length = 0

        while len(queue) != 0:
            current_node = queue.pop(0)

            if current_node == panda2:
                found = True
                break

            for neighbour in self.pandas[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)

        if found:
            while path_to[panda2] is not None:
                path_length += 1
                panda2 = path_to[panda2]

        return path_length

    def are_connected(self, panda1, panda2):
        level_conn = PandaSocialNetwork.connection_level(self, panda1, panda2)

        return level_conn > 0

    def how_many_gender_in_network(self, level, panda, gender):
        counter = 0
        conn_level = 0

        for panda_user in self.pandas:
            conn_level = PandaSocialNetwork.connection_level(
                self, panda, panda_user)

            different_panda = panda_user != panda
            bigger_or_equal_level = conn_level <= level
            same_gender = panda_user.get_gender() == gender

            if different_panda and bigger_or_equal_level and same_gender:
                counter += 1

        return counter

    def save_social_network(self, file_name):
        all_pandas = {}
        for panda in self.pandas:
            all_pandas[repr(panda)] = []

            for friend_of_panda in self.pandas[panda]:
                all_pandas[repr(panda)] += [repr(friend_of_panda)]

        with open(file_name, "w") as file_to_save:
            json.dump(all_pandas, file_to_save)

    def load_social_network(self, file_name):
        with open(file_name, "r") as file_to_load:
            all_pandas = json.loads(file_to_load.read())

        all_friends = []
        for panda in all_pandas:
            self.pandas[eval(panda)] = []

            for friend_of_panda in all_pandas[panda]:
                all_friends += [eval(friend_of_panda)]

            self.pandas[eval(panda)] = all_friends
            all_friends = []
