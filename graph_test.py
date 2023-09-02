"""
graph_test.py.

Starter test file for the graph module. Add your own tests to this
file.

Project UID bd3b06d8a60861e18088226c3a1f0595e4426dcf
"""

import graph


def undirected_test():
    """Run basic tests on an undirected graph."""
    ugraph = graph.read_graph_from_csv('characters-nodes.csv',
                                       'characters-edges.csv')
    assert ugraph.degree('0') == 6
    assert '0' in ugraph
    assert len(ugraph) == 10
    assert ('0', '2') in ugraph
    assert ('2', '0') in ugraph
    print(', '.join(n.identifier() for n in ugraph.nodes()))
    print(ugraph)


def simple_directed_graph():
    """Build a simple directed graph."""
    dgraph = graph.DirectedGraph()
    dgraph.add_node(0, airport_name='DTW')
    dgraph.add_node(1, airport_name='AMS', country='The Netherlands')
    dgraph.add_node(2, airport_name='ORD', city='Chicago')
    dgraph.add_edge(0, 1, flight_time_in_hours=8)
    dgraph.add_edge(0, 2, flight_time_in_hours=1)
    dgraph.add_edge(1, 0, airline_name='KLM')
    return dgraph


def directed_test():
    """Run basic tests on a directed graph."""
    dgraph = simple_directed_graph()
    assert dgraph.in_degree(2) == 1
    assert dgraph.out_degree(0) == 2
    print(dgraph)


# add more test cases here
def graph_node_test():
    """Basic test on nodes of graph"""
    graph1 = graph.UndirectedGraph()
    graph2 = graph.DirectedGraph()
    graph1.add_node(1,  name='node1')
    graph1.add_node(2,  name='node2')
    graph2.add_node(1, name = 'node1')
    graph2.add_node(2, name = 'node2')
    assert(len(graph1) == 2)
    assert(len(graph2) == 2)
    assert(1 in graph1)
    assert(2 in graph1)
    assert(1 in graph2)
    assert(2 in graph2)

def directed_graph_edge_test():
    graph1 = graph.DirectedGraph()
    graph1.add_node(1,  name='Milan')
    graph1.add_node(2,  name='Rome')
    graph1.add_node(3,  name='Naples')
    graph1.add_edge(1, 2, train='Italo')
    graph1.add_edge(2, 3, train='Frecciarossa')
    assert((1, 2) in graph1)
    assert((2, 3) in graph1)
    assert((2, 1) not in graph1)
    assert((3, 2) not in graph1)
    assert((1, 1) not in graph1)
    assert((1, 6) not in graph1)
    assert(graph1.in_degree(1) == 0)
    assert(graph1.in_degree(2) == 1)
    assert(graph1.in_degree(3) == 1)
    assert(graph1.out_degree(1) == 1)
    assert(graph1.out_degree(2) == 1)
    assert(graph1.out_degree(3) == 0)

def undirected_graph_edge_test():
    graph1 = graph.UndirectedGraph()
    graph1.add_node(1,  name='Milan')
    graph1.add_node(2,  name='Rome')
    graph1.add_node(3,  name='Naples')
    graph1.add_edge(1, 2, train='Italo')
    graph1.add_edge(2, 3, train='Frecciarossa')
    assert((1, 2) in graph1)
    assert((2, 3) in graph1)
    assert((2, 1) in graph1)
    assert((3, 2) in graph1)
    assert(graph1.degree(1)==1)
    assert(graph1.degree(2)==2)
    assert(graph1.degree(3)==1)


if __name__ == '__main__':
    undirected_test()
    directed_test()
    graph_node_test()
    directed_graph_edge_test()
    undirected_graph_edge_test()
    # call test cases from here
