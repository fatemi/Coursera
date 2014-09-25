# if required change your current directory:
# import os
# os.chdir('/Users/mehdifatemi/Dropbox/Python/NetworkX/Coursera/')

G = nx.read_gml('26KeroGephiFileClean.gml')
print(nx.info(G))

# for clustering, G should be treated as an undirected graph:
ccv = nx.clustering(G.to_undirected())  
# sorting cvv (ascending):
v = sorted(ccv.values())

# removing all the zero clustering coefficients;
# at each iteration if v[0] is zero, it will be deleted, till reaching the first non-zero element
while v[0]==0: del(v[0])
    
print('minimum clust. coef. = ', min(v))
print('maximum clust. coef. = ', max(v))
