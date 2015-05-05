from exceptions import NodeNotInNodesException
from exceptions import CantAddEgdeToTheSameNodeException
from exceptions import CantAddSameNodeException


class DirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node in self.nodes:
            raise CantAddSameNodeException
        self.nodes[node] = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.nodes:
            self.add_node(node_a)

        if node_b not in self.nodes:
            self.add_node(node_b)

        if node_a == node_b:
            raise CantAddEgdeToTheSameNodeException

        self.nodes[node_a].append(node_b)

    def get_neighbors_for(self, node):
        if node in self.nodes:
            return self.nodes[node]
        else:
            raise NodeNotInNodesException

    def edge_between(self, node_a, node_b):
        return node_b in self.nodes[node_a]

    def path_between(self, node_a, node_b):
        visited = set()
        queue = []

        visited.add(node_a)
        queue.append(node_a)

        is_there_path = False

        while len(queue) != 0:
            current_node = queue.pop(0)

            if current_node == node_b:
                is_there_path = True
                break

            for neighbour in self.nodes[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return is_there_path
