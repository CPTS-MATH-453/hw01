from SpanningBipartiteGraph import *

def sbg(g):
    # TODO: Find a spanning bipartite graph g[X, Y] such that |E(F)| ≥ 1/2 |E(G)|.
    # Input: Graph g.
    # Output: subset X.
    set_X = set()


    return set_X


if __name__ == "__main__":
    test_graph = Graph(4)
    # test_graph.print_graph()
    test_graph.add_edge(1,2)
    test_graph.add_edge(3,0)
    test_graph.add_edge(1,0)
    test_graph.add_edge(3,2)
    test_graph.add_edge(3,2)
    sb_graph = SpanningBipartiteGraph(sbg(test_graph), test_graph)
    sb_graph.print_graph()
    print("Number of edges is", sb_graph.num_edges())
