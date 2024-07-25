from collections import deque


class SimpleGraph:
    
    def __init__(self) -> None:
        self._g = dict()

    def add_vertex(self, vertex_id) -> str:
        """
        Adds a vertex to the graph.

        Parameters:
            vertex_id (str): ID/name of vertex.

        Example:
            g = Graph()
            g.add_vertex("GRU")    # "GRU"

        Raises:
            ValueError: If a vertex with same ID/name already exists.

        Returns:
            str: ID/name of the newly added vertex.
        """
        if vertex_id in self:
            raise ValueError(f"Vertex '{vertex_id}' already exists!")
        
        self._g[vertex_id] = set()

        return vertex_id

    def get_vertices(self) -> set:
        """
        Returns all vertices of the graph.

        Examples:
            g = Graph()
            g.add_vertex('A')    # A
            g.add_vertex('B')    # B
            g.add_vertex('C')    # C

            g.get_vertices()     # {'A', 'B', 'C'}

        Returns:
            set: All vertices of the graph.
        """
        return self._g.keys()

    def add_edge(self, from_vertex, to_vertex) -> str:
        """
        Adds an edge that connects `from_vertex` to `to_vertex`.
        Vertices will be created if they don't exist yet.

        Parameters:
            from_vertex (str): Origin vertex.
            to_vertex (str): Destination vertex.

        Examples:
            g = Graph()
            g.add_edge('A', 'B')   # A -> B
            g.add_edge('A', 'C')   # A -> C

        Returns:
            str: String representation of the edge.
        """
        if from_vertex not in self:
            self.add_vertex(from_vertex)

        if to_vertex not in self:
            self.add_vertex(to_vertex)

        self._g[from_vertex].add(to_vertex)

        return from_vertex, to_vertex

    def exists_path(self, from_vertex, to_vertex) -> bool:
        to_search = deque()
        to_search += self._g[from_vertex]

        searched = set()

        while to_search:
            current_vertex = to_search.popleft()
            
            if current_vertex not in searched:
                
                if current_vertex == to_vertex:
                    # Path found
                    return True

                to_search += self._g[current_vertex]

                searched.add(current_vertex)

        # No path found
        return False

    def is_empty(self) -> bool:
        return len(self._g) == 0
    
    def __len__(self) -> int:
        return len(self._g)
    
    def __contains__(self, vertex_id) -> bool:
        return vertex_id in self._g
