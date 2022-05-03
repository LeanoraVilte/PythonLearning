import pandas as pd

from pandas import DataFrame, Series
import matplotlib.pyplot as plt

s: Series = pd.Series([7, 6, 5, 4, 5, 3, 2, 1])

s.plot(kind='bar')
