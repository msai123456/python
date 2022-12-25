import numpy as np
revenue=np.array([[12,2,2],[1,2,9]])
expence=np.array([[80,90,100],[8,10,12]])

# dot matrix (multiply the row and column)
total=revenue+expence
print(total)

# to check the demension using ndim in numpy
print(revenue.ndim)