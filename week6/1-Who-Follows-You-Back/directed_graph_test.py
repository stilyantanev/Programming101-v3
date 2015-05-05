import unittest
from directed_graph import DirectedGraph
from exceptions import CantAddSameNodeException
from exceptions import NodeNotInNodesException
from exceptions import CantAddEgdeToTheSameNodeException


class DirectGraphTest(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_make_instance(self):
        self.assertTrue(isinstance(self.graph, DirectedGraph))

    def test_valid_instance_members(self):
        self.assertEqual(self.graph.nodes, {})

    def test_add_node_which_is_in_graph(self):
        self.graph.nodes["Ivan"] = []
        with self.assertRaises(CantAddSameNodeException):
            self.graph.add_node("Ivan")

    def test_add_node_which_is_not_in_graph(self):
        self.graph.add_node("Ivan")
        self.assertEqual(self.graph.nodes["Ivan"], [])

    def test_add_edge_between_nodes_not_in_graph(self):
        self.graph.add_edge("Ivan", "Pesho")
        self.assertEqual(self.graph.nodes["Ivan"], ["Pesho"])

    def test_add_edge_between_nodes_in_graph(self):
        self.graph.nodes["Ivan"] = []
        self.graph.nodes["Pesho"] = []
        self.graph.add_edge("Ivan", "Pesho")
        self.assertEqual(self.graph.nodes["Ivan"], ["Pesho"])

    def test_add_edge_between_same_nodes(self):
        with self.assertRaises(CantAddEgdeToTheSameNodeException):
            self.graph.add_edge("Ivan", "Ivan")

    def test_get_neighbors_for_node_in_graph(self):
        self.graph.nodes["Ivan"] = ["Pesho"]
        self.assertEqual(self.graph.get_neighbors_for("Ivan"), ["Pesho"])

    def test_get_neighbors_for_node_not_in_graph(self):
        with self.assertRaises(NodeNotInNodesException):
            self.graph.get_neighbors_for("Ivan")

    def test_edge_between_connected_nodes(self):
        self.graph.nodes["Ivan"] = ["Pesho"]
        self.assertTrue(self.graph.edge_between("Ivan", "Pesho"))

    def test_edge_betwenn_not_connected_nodes(self):
        self.graph.nodes["Ivan"] = ["Pesho"]
        self.assertFalse(self.graph.edge_between("Ivan", "Valio"))

    def test_path_between_nodes_that_are_not_connected(self):
        self.graph.nodes["Ivan"] = ["Valio", "Gosho"]
        self.graph.nodes["Valio"] = ["Dimitur", "Stilyan"]
        self.graph.nodes["Valio"] = []
        self.graph.nodes["Gosho"] = []
        self.graph.nodes["Dimitur"] = []
        self.graph.nodes["Stilyan"] = []
        self.assertFalse(self.graph.path_between("Gosho", "Dimitur"))

    def test_path_between_nodes_that_are_connected(self):
        self.graph.nodes["Ivan"] = ["Valio"]
        self.graph.nodes["Valio"] = ["Dimitur", "Stilyan"]
        self.graph.nodes["Dimitur"] = []
        self.graph.nodes["Stilyan"] = []
        self.assertTrue(self.graph.path_between("Ivan", "Stilyan"))

if __name__ == '__main__':
    unittest.main()
