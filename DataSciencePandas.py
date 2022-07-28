import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.style.use('ggplot')

df = pd.read_csv("Test1.csv")
x = df['city']

s: Series = pd.Series([7, 6, 5, 4, 5, 3, 0, 0, 1])

s.plot(kind='bar')

fig = plt.figure()
ax = plt.axes()
plt.show()
