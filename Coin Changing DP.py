#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import time


# In[14]:


def change(coin:list, amount: int) :
    coin.sort()
    row = len(coin)
    col = amount + 1
    table = (row,col)
    matrix = np.zeros(table)
    
    I = 0
    for I in range(col):
        matrix[0][I] = int(I)
    
    i = 1                 
    while (i < row) :
        j = 1
        while (j <col):
            if (j < coin[i]) :
                matrix[i][j] = int(matrix[i-1][j])
            else :
                matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j - coin[i]] + 1))
            j+=1
        i+=1

    df = pd.DataFrame(matrix)
    w = col
    h = row
    plt.figure(1, figsize=(w, h))
    tb = plt.table(cellText=matrix, loc=(0,0), cellLoc='center')

    tc = tb.properties()['child_artists']
    for cell in tc: 
        cell.set_height(1.0/row)
        cell.set_width(1.0/col)

    ax = plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])
#     ax = sns.heatmap(matrix, annot=True, fmt="f")
    plt.show()    
        
#     print(matrix)
    print("minimum coin : ", end = '')
    print(int(matrix[row-1][col-1]))

    a = row - 1             
    b = col - 1
    count = 0
    cek = 0
    print("You receive : ", end = '')
    while (a > 0 and b > 0) :
        if (matrix[a-1][b] == matrix[a][b]) :
            a -= 1
            continue
        print(coin[a], end = ' ')
        b -= coin[a]
        amount -= coin[a]
        count += 1
    
    if (count != matrix[row-1][col-1]) :
        print(coin[a])
        amount -= coin[a]

    if (amount != 0) :
        print("Coin cannot be exchanged")


# In[15]:


# %%time
start = time.time()
amount = int (input("Coin you want to exchange : "))
if (amount > 0) :
    n = int(input("How many coins are available : "))
    coin = []
    for x in range(n):
        coin.append(int(input("Input : ")))
    change(coin, amount)
else :
    print("Coin cannot be exchanged")
    
end = time.time()
print()
print("Execution time : ", end = '')
print(end - start)

