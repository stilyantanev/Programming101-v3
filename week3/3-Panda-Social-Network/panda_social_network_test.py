import unittest
from panda_social_network import Panda
from panda_social_network import PandaSocialNetwork
from panda_exceptions import PandaEmailException
from panda_exceptions import PandaAlreadyThereException
from panda_exceptions import PandasAlreadyFriendsException


class PandaTest(unittest.TestCase):

    def setUp(self):
        self.panda = Panda("Georgi", "Georgi123@abv.bg", "male")

    def test_create_new_panda_instance(self):
        self.assertTrue(isinstance(self.panda, Panda))

    def test_valid_members_panda(self):
        self.assertEqual(self.panda.name, "Georgi")
        self.assertEqual(self.panda.email, "Georgi123@abv.bg")
        self.assertEqual(self.panda.gender, "male")

    def test_valid_email(self):
        with self.assertRaises(PandaEmailException):
            Panda("Georgi", "Georgi123abvbg", "male")

    def test_get_name(self):
        self.assertEqual(self.panda.get_name(), "Georgi")

    def test_get_email(self):
        self.assertEqual(self.panda.get_email(), "Georgi123@abv.bg")

    def test_get_gender(self):
        self.assertEqual(self.panda.get_gender(), "male")

    def test_is_male(self):
        self.assertTrue(self.panda.isMale())

    def test_is_female(self):
        self.assertFalse(self.panda.isFemale())

    def test_str_cast(self):
        panda_gender = self.panda.gender
        panda_name = self.panda.name
        panda_email = self.panda.email

        message = "I am {} panda, my name is {}, for contacts: {}"
        message = message.format(panda_gender, panda_name, panda_email)

        self.assertEqual(str(self.panda), message)

    def test_check_equal(self):
        self.another_panda = Panda("Georgi", "Georgi123@abv.bg", "male")

        self.assertEqual(self.panda.name, self.another_panda.name)
        self.assertEqual(self.panda.email, self.another_panda.email)
        self.assertEqual(self.panda.gender, self.another_panda.gender)

        self.assertTrue(self.panda == self.another_panda)

    def test_hash(self):
        panda_gender = self.panda.gender
        panda_name = self.panda.name
        panda_email = self.panda.email
        hash_code = hash(panda_gender + panda_name + panda_email)
        self.assertTrue(isinstance(hash_code, int))


class PandaSocialNetworkTest(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()

    def test_create_new_panda_social_network_instance(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_valid_members(self):
        self.assertEqual(self.network.pandas, {})

    def test_duplicate_panda(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        another_panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        self.network.pandas = {panda: [], another_panda: []}

        with self.assertRaises(PandaAlreadyThereException):
            self.network.add_panda(panda)

    def test_add_panda_in_network(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        self.network.add_panda(panda)
        self.assertTrue(panda in self.network.pandas)

    def test_has_panda_in_network(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        another_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        self.network.add_panda(panda)
        self.assertTrue(self.network.has_panda(panda))
        self.assertFalse(self.network.has_panda(another_panda))

    def test_has_not_panda_in_network(self):
        another_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        self.assertFalse(self.network.has_panda(another_panda))

    def test_already_friends(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        another_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        self.network.add_panda(panda)
        self.network.add_panda(another_panda)
        self.assertTrue(self.network.has_panda(panda))
        self.assertTrue(self.network.has_panda(another_panda))
        self.network.make_friends(panda, another_panda)
        with self.assertRaises(PandasAlreadyFriendsException):
            self.network.make_friends(panda, another_panda)

    def test_make_friends(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        other_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        self.network.add_panda(panda)
        self.network.add_panda(other_panda)
        self.assertTrue(self.network.has_panda(panda))
        self.assertTrue(self.network.has_panda(other_panda))
        self.network.make_friends(panda, other_panda)
        result = {panda: [other_panda],
                  other_panda: [panda]}
        self.assertEqual(self.network.pandas, result)

    def test_are_friends(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        other_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        another_panda = Panda("Grisha", "ggg@abv.bg", "male")
        self.network.add_panda(panda)
        self.network.add_panda(other_panda)
        self.network.add_panda(another_panda)
        self.network.make_friends(panda, other_panda)
        self.assertTrue(self.network.are_friends(panda, other_panda))
        self.assertFalse(self.network.are_friends(panda, another_panda))

    def test_friends_of_panda_not_in_network(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        self.assertFalse(self.network.friends_of(panda))

    def test_friends_of_panda_in_network(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        self.network.add_panda(panda)
        self.assertEqual(self.network.friends_of(panda), [])

    def test_connection_level(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        other_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        self.network.add_panda(panda)
        self.network.add_panda(other_panda)
        self.assertEqual(self.network.connection_level(panda, other_panda), 0)

    def test_are_not_connected_friends(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        other_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        self.network.add_panda(panda)
        self.network.add_panda(other_panda)
        self.assertFalse(self.network.are_connected(panda, other_panda))

    def test_how_many_gender_in_network(self):
        panda = Panda("Georgi", "Georgi123@abv.bg", "male")
        other_panda = Panda("Pesho", "pesho128@abv.bg", "male")
        another_panda = Panda("Grisha", "ggg@abv.bg", "male")
        self.network.add_panda(panda)
        self.network.add_panda(other_panda)
        self.network.add_panda(another_panda)
        self.assertEqual(
            self.network.how_many_gender_in_network(1, panda, "male"), 2)

if __name__ == '__main__':
    unittest.main()
