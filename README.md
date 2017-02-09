# Fast density clustering
Python code for clustering two dimensional data using kernel density maps to construct a density graph. Examples for gaussian mixtures and some benchmarks are provided. Our algorithm solves multiscale problems (multiple variances/densities and population sizes) and works for non-convex clusters. It uses cross-validation and is regularized by two main global parameters : a neighborhood
size and a noise threshold measure. The later detects spurious cluster centers while the former guarantees that only local information is used to infer cluster centers (we avoid using long distance information). 

The underlying code is based on fast KD-trees for nearest-neighbor searches O(n log n). While the algorithm is well suited for small datasets with meaningful densities, it works quite well on large datasets (c.g. for N=10000, run time is a few seconds).

# Running

Clone or download this repository and run the following command inside the top directory:

```
pip3 install .
```
That's it ! 
# Examples and comparison with other methods
Check out the example for gaussian mixtures (example.py). You should be able to run it directly. It
should produce a plot similar to this: ![alt tag](https://github.com/alexandreday/fast_density_clustering/blob/master/example/result.png)

In another example (example2.py), the algorithm is benchmarked against some sklearn datasets (note that the same parameters are used across all datasets). This is to be compared with other clustering methods easily accesible from [sklearn](http://scikit-learn.org/stable/modules/clustering.html). ![alt tag](https://github.com/alexandreday/fast_density_clustering/blob/master/example/sklearn_datasets.png)
# Citation

If you use this code in a scientific publication, I would appreciate citation/reference to this repository
