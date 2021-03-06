'''
Created on Feb 4, 2017

@author: Alexandre Day

    Perform density clustering on some datasets found in the sklearn 
    documentation on clustering (http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)
'''

import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from fdc import FDC, plotting


np.random.seed(0)

# ============
# Generate datasets. We choose the size big enough to see the scalability
# of the algorithms, but not too big to avoid too long running times
# ============
n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5,
                                      noise=.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

# Anisotropicly distributed data
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

# blobs with varied variances
varied = datasets.make_blobs(n_samples=n_samples,
                             cluster_std=[1.0, 2.5, 0.5],
                             random_state=random_state)

colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = np.hstack([colors] * 20)

plot_num = 1

fig= plt.figure(figsize=(7, 10))

#################################
#################################
#################################
#################################


"""
Setting FDC parameters (note these are the same across all datasets)
"""

datasets = [noisy_circles, noisy_moons, varied, aniso, blobs, no_structure]
for i_dataset, dataset in enumerate(datasets):
    X, y = dataset
    # normalize dataset for easier parameter selection
    X = StandardScaler().fit_transform(X)

    # create clustering estimators
    # atol and rtol set the precision of the density map, higher value improves performanc but reduces accuracy
    model = FDC(eta=0.4)

    s=time.time()

    model.fit(X)

    dt=time.time()-s

    n_center=len(model.idx_centers)

    plt.subplot(3,2,plot_num)
    plt.scatter(X[:, 0], X[:, 1], color=colors[model.cluster_label].tolist(), s=10,zorder=1)

    plt.text(.99, .07, ('%.2fs' % (dt)).lstrip('0'),
                 transform=plt.gca().transAxes, size=15,
                 horizontalalignment='right',zorder=2,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.1')
                 )

    plot_num+=1

plt.suptitle("Local density clustering with %s kernels \n Number of data points = %i"%(model.kernel,n_samples))

plt.savefig("sklearn_datasets.png")
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
