from lib.graph_simple import SimpleGraph


def test_empty_true():
    graph = SimpleGraph()
    
    assert graph.is_empty()


def test_empty_false():
    graph = SimpleGraph()
    graph.add_vertex('A')

    assert not graph.is_empty()


def test_add_vertex():
    graph = SimpleGraph()
    graph.add_vertex('A')

    assert not graph.is_empty()
    assert len(graph) == 1
    assert 'A' in graph
    assert 'B' not in graph


def test_get_vertices():
    graph = SimpleGraph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')

    edges = graph.get_vertices()
    
    assert len(edges) == 3
    assert 'A' in edges
    assert 'B' in edges
    assert 'C' in edges


def test_add_edge():
    graph = SimpleGraph()

    assert graph.add_edge('A', 'B') == ('A', 'B')
    assert graph.add_edge('B', 'C') == ('B', 'C')
    assert graph.add_edge('C', 'A') == ('C', 'A')

    assert len(graph) == 3
    assert 'A' in graph
    assert 'B' in graph
    assert 'C' in graph



def test_exists_path():
    graph = SimpleGraph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('D', 'E')
    graph.add_edge('E', 'F')

    assert graph.exists_path('A', 'B')
    assert graph.exists_path('A', 'C')
    assert graph.exists_path('B', 'D')
    assert graph.exists_path('B', 'E')
    assert graph.exists_path('A', 'D')
    assert graph.exists_path('A', 'E')
    assert graph.exists_path('A', 'F')
    assert not graph.exists_path('C', 'E')
    assert not graph.exists_path('B', 'C')
    assert not graph.exists_path('F', 'E')
    assert not graph.exists_path('E', 'A')
