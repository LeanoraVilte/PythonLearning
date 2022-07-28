import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series
import numpy as np
import matplotlib.pyplot as plt

# Open the file in read mode. If encoding is an issue, specify the correct encoding here.
from contourpy.util import data

with open('Test1.csv', mode='r', encoding='UTF8') as file:

    # Read CSV file. Specify the correct delimiter and how to handle quotation marks.
    lines = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONE)

    # Exctract header.
    #header = next(data)
    ... # Check if the header complies to your data model.

    # Loop through body.
    a = []
    for line in lines:
        a.append(line)

    #print(a)

    a1 = np.array((a[0], a[1]))
    df = pd.DataFrame(a1)
    s = df[2]
    s2 = df[1]

    plt.style.use('ggplot')
    s1 = s.astype(int)
    s1.plot(kind = 'pie')
    #plt.scatter(s1, s2 m, arker='<', color='r')
    #plt.xlabel('city')
    #plt.ylabel('county')
    plt.show()


    print(s)