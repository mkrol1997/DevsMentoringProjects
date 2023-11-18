from typing import List


class Graph:
    def __init__(self):
        self._matrix: List[List[int]] = []
        self._graph_length: int = 0

    @property
    def graph_length(self) -> int:
        return self._graph_length

    def add_vertex(self):
        """
        Adds Vertex index to the Adjacency Matrix
        """

        self._graph_length += 1

        for vertices in self._matrix:
            vertices.append(0)

        self._matrix.append([0] * self._graph_length)

    def add_edge(self, start: int, end: int, weight: int) -> None:
        """
        Adds an edge between two vertices in the graph with the specified weight.
        """

        if start < 0 or end >= len(self._matrix):
            raise IndexError(f"Invalid index. Choose from 0 - {len(self._matrix) - 1}")

        self._matrix[start][end] = weight

    def print_neighbors(self, vertex_id: int) -> None:
        """
        Prints the neighbors of a vertex by their IDs along with their connections.
        """

        if vertex_id not in range(0, len(self._matrix)):
            raise IndexError(f"Invalid index. Choose from 0 - {len(self._matrix) - 1}")

        vertex = self._matrix[vertex_id]
        vertex_neighbors = [str(nbr_id) for nbr_id, weight in enumerate(vertex) if weight != 0]

        print("Vertex {} is connected to: {}".format(vertex_id, ", ".join(vertex_neighbors)))

    def get_neighbours(self, vertex_id) -> List[int]:
        """
        Returns a list of Vertices IDs representing the neighboring vertices of the specified vertex.
        """

        return [nbr_id for nbr_id, weight in enumerate(self._matrix[vertex_id]) if weight != 0]

    def show_graph(self) -> None:
        """
        Prints the connections of all vertices in the graph.
        """

        for vertex_id in range(self._graph_length):
            self.print_neighbors(vertex_id)


def main():
    graph = Graph()

    for _ in range(8):
        graph.add_vertex()

    graph.add_edge(0, 2, 1)
    graph.add_edge(0, 5, 6)
    graph.add_edge(0, 4, 2)
    graph.add_edge(1, 4, 10)
    graph.add_edge(1, 5, 8)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 1, 1)
    graph.add_edge(3, 4, 1)
    graph.add_edge(4, 2, 3)
    graph.add_edge(4, 5, 2)
    graph.add_edge(5, 3, 4)
    graph.add_edge(5, 7, 2)
    graph.add_edge(6, 3, 4)
    graph.add_edge(6, 5, 1)
    graph.add_edge(7, 2, 8)
    graph.add_edge(7, 6, 2)
    graph.add_edge(7, 3, 13)

    graph.show_graph()


if __name__ == "__main__":
    main()
