from modules.parser import Parser
from structs.graph import Graph
from scripts.load_data import parse_html
import time


def make_graph(path):
    print("\n Ucitavanje graph\n")
    edge_list=list()
    graph=Graph()
    parser=Parser()
    begin_time=time.time()
    parse_html(path,edge_list)
    list_vertex=set()
    for edge in edge_list:
        list_vertex.add(edge[0])
        list_vertex.add(edge[1])

    for v in list_vertex:
        graph.insert_vertex(v)
    for edge in edge_list:
        in_ver=edge[0]
        out_ver=edge[1]

        graph.insert_edge(in_ver,out_ver)

    print("\n Ucitan graph za %s sekundi "%(time.time()-begin_time))
    return graph

