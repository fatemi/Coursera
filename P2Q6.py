'''
Problem set 2; Question 6:

'''

import networkx as nx
import numpy as np

# change the current directory if necessary:
# import os
# os.chdir('/Users/mehdifatemi/Desktop/')

G = nx.read_pajek('imports_manufactures.net')
# treated the imported multi-graph as a directed graph:
G = nx.DiGraph(G) 
print(nx.info(G))

# closeness centrality measure:
cl_centrality = nx.closeness_centrality(G)
# finding the maximum:
cl_cnt_sorted = sorted(cl_centrality, key=cl_centrality.get, reverse=True)
print('Country with maximum closeness centrality: ', cl_cnt_sorted[0])

bt_centrality = nx.betweenness_centrality(G)
bt_cnt_sorted = sorted(bt_centrality, key=bt_centrality.get, reverse=True)
print('Country with maximum betweenness centrality: ', bt_cnt_sorted[0])
