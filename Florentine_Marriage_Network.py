import networkx as nx
import numpy as np

# Making a graph:
G = nx.Graph()

# nodes:
nodes = np.arange(1,16) # only 15 nodes, ignoring pucci
G.add_nodes_from(nodes)
G.node[1]['name'] = 'CASTELLAN'
G.node[2]['name'] = 'PERUZZI'
G.node[3]['name'] = 'STROZZI'
G.node[4]['name'] = 'BECHERI'
G.node[5]['name'] = 'GUADAGNI'
G.node[6]['name'] = 'LAMBERTES'
G.node[7]['name'] = 'RIDOLFI'
G.node[8]['name'] = 'BARBADORI'
G.node[9]['name'] = 'TORNABUON'
G.node[10]['name'] = 'MEDICI'
G.node[11]['name'] = 'SALVIATI'
G.node[12]['name'] = 'PAZZI'
G.node[13]['name'] = 'ACCAUOL'
G.node[14]['name'] = 'ALBIZZI'
G.node[15]['name'] = 'GINORI'

# edges:
edge_list = [(1,2),
         (1,3),
         (1,8),
         (2,3),
         (2,4),
         (3,4),
         (3,7),
         (4,5),
         (5,6),
         (5,9),
         (5,14),
         (7,9),
         (7,10),
         (8,10),
         (9,10),
         (10,11),
         (10,13),
         (10,14),
         (11,12),
         (14,15)]

G.add_edges_from(edge_list)
