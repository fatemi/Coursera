'''
A good practice for Problem Set 2; Question 3

'''

import networkx as nx
import numpy as np

# Making a graph:
G = nx.Graph()
# nodes:
nodes = np.arange(1,8) # only 15 nodes, ignoring pucci
G.add_nodes_from(nodes)
# edges:
edge_list = [(1,4),
         (1,7),
         (2,4),
         (2,5),
         (3,5),
         (4,7),
         (6,7)]
G.add_edges_from(edge_list)
nx.betweenness_centrality(G)
