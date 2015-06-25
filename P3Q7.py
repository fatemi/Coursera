'''
Problem Set 3; Question 7

Run the following code:

'''

import numpy as np
import networkx as nx
from matplotlib.pyplot import *
'''
# change the working directory if necessary:
import os 
os.chdir('/Users/mehdifatemi/Desktop/')
'''

G = nx.read_pajek('Ring25.NET')
G = nx.Graph(G)
print(nx.info(G))

print('Diameter: ', nx.diameter(G))
print('Average Clustering: ', nx.average_clustering(G))
