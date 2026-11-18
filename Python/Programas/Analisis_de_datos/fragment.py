import numpy as np 

data = np.array([100,200,300,400,500])
sample = data[1:4]
sample[0] = 0
print("Original data: ",data)

x = np.random.rand(50,10)
row_means = np.mean(x, axis = 1)
x_centered = x - row_means

temperatures = np.array([[20,22,25],[18,21,23],[19,20,22]])