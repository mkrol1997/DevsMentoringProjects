from typing import List

from graph import Graph


class Vertex:
    def __init__(self, vertex_id):
        self.__vertex_id = vertex_id
        self.is_visited = False

    @property
    def vertex_id(self):
        return self.__vertex_id

    def __str__(self):
        return f"{self.__vertex_id}"


class BFSGraph(Graph):
    def __init__(self):
        """
        Initializes Graph and adds list of Vertices
        """
        super().__init__()
        self.__vertices: List[Vertex] = []

    @property
    def vertices(self):
        return self.__vertices

    def add_vertex(self):
        """
        Adds Vertex index both to the Adjacency Matrix and list of Graph Vertices
        """
        self.vertices.append(Vertex(self._graph_length))
        super().add_vertex()


class BreadthFirstSearch:
    def __init__(self, graph: BFSGraph) -> None:
        self.__queue: List[Vertex] = []
        self.__graph = graph

    def add_neighbours(self, parent_id: int) -> None:
        """
        Adds neighbours of a given vertex to the traversal queue.
        """
        neighbours = self.__graph.get_neighbours(parent_id)
        [self.__queue.append(self.__graph.vertices[neighbour_id]) for neighbour_id in neighbours]

    def traverse(self) -> None:
        while self.__queue:
            curr_vertex = self.__queue.pop(0)

            if not curr_vertex.is_visited:
                self.add_neighbours(curr_vertex.vertex_id)
                curr_vertex.is_visited = True
                print(f'Visited Vertex: {curr_vertex.vertex_id}')

    def run(self, start_vertex_id: int) -> None:
        """
        Initializes BFS traversal from a specified starting vertex.
        """
        starting_vertex = self.__graph.vertices[start_vertex_id]
        self.__queue.append(starting_vertex)
        self.traverse()


def main():
    graph = BFSGraph()

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

    dfs = BreadthFirstSearch(graph)
    dfs.run(0)


if __name__ == '__main__':
    main()
