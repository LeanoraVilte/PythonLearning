import numpy as np
from numpy import mean

from midle_test import middle

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1])
y = mean(x)
z = middle(x)

print(y)
print(z)
