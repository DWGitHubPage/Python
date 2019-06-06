# Python3.7.3

import pandas as plt
from pandas import DataFrame
from sklearn.datasets.samples_generator import make_blobs

# Generate 2D data points.
x, _ = make_blobs(n_samples=10, centers=3, n_features=3,
                 cluster_std=0.5,  random_state=0)


obj_names = []
for i in range(1, 11):
    obj = "object " + str(i)
    obj_names.append(obj)

data = plt.DataFrame({
    'object': obj_names,
    'x_value': x[:, 0],
    'y_value': x[:, -1]
})

print(data.head())

# Second example of data.

Data = {'x': [12,24,32,37,45,34,35,50,53,56,58,59,5,4,60,62,64,65,66,67,68,69,35,33],
        'y': [10,15,20,22,24,26,28,30,33,37,39,41,43,47,50,52,35,35,38,42,44,45,46, 49]
       }
  
df = DataFrame(Data,columns=['x','y'])

print(df)
