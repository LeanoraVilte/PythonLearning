from math import floor

import numpy as np
from numpy import mean, std
from numpy import floor

from midle_test import middle

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1])
y = mean(x)
z = middle(x)
r = sum(x)
u = floor(x)
s = std(x)

def In_std(x):
    a = []
    i = 0
    y = len(x)
    for i in range(y):
        if abs(mean(x) - x[i]) <= s:
            a.append(x[i])
        i += 1
    return (a)



print(r)
print(y)
print(z)
print(u)
print(s)

print(In_std(x))