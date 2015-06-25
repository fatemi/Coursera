'''
Problem set 2; Question 8:

Note that a connected network has only one component!
Hence, what we do is to find the number of components in each of the four
graphs and then average it over a large-enough number of experiments
(50 in this code). The run may take a few seconds depending on your computer's
CPU clock speed.

'''


import networkx as nx
import numpy as np

# number of experiments:
num_experiments = 50 

# initializing variables for number of components in each graphs
num_component_G1 = 0
num_component_G2 = 0
num_component_G3 = 0
num_component_G4 = 0

for count in range(num_experiments):
    # 400 nodes and average degree = 1
    n = 400
    avg_degree = 1
    p = avg_degree/(n-1)
    G1 = nx.erdos_renyi_graph(n, p)
    num_component_G1 += len(nx.connected_component_subgraphs(G1))
    
    # 400 nodes and average degree = 5
    n = 400
    avg_degree = 5
    p = avg_degree/(n-1)
    G2 = nx.erdos_renyi_graph(n, p)
    num_component_G2 += len(nx.connected_component_subgraphs(G2))

    # 400 nodes and average degree = 10
    n = 400
    avg_degree = 10
    p = avg_degree/(n-1)
    G3 = nx.erdos_renyi_graph(n, p)
    num_component_G3 += len(nx.connected_component_subgraphs(G3))

    # 400 nodes and average degree = 20
    n = 400
    avg_degree = 20
    p = avg_degree/(n-1)
    G4 = nx.erdos_renyi_graph(n, p)
    num_component_G4 += len(nx.connected_component_subgraphs(G4))
    
print('G1 :: ', num_component_G1 / num_experiments)
print('G2 :: ', num_component_G2 / num_experiments)
print('G3 :: ', num_component_G3 / num_experiments)
print('G4 :: ', num_component_G4 / num_experiments)
