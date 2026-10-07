import numpy as np

lst = list(range(10))
arr = np.arange(10)

%timeit sum(lst)

np.sum(arr)