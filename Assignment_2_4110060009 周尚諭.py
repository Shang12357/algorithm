# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:10:51 2024

@author: shang
"""

import numpy
import matplotlib.pyplot as plt
import time

#%%
#top down
def fib_top_down(n):
    if n <= 1:
        return n
    
    else:
        return fib_top_down(n - 1) + fib_top_down(n - 2)
    



#botton up
def fib_bottom_up(n):

    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[0] = 1
    table[1] = 1
    
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


# n = 10  
# print(f"Fibonacci({n}) =", fib_top_down(n))
# print(f"Fibonacci({n}) =", fib_bottom_up(n))


#Q1
topdown = []
bottomup = []
x = []

t0 = time.time()

for i in range(50):
    print(i)
    try:
        t1 = time.time()
        fib_top_down(i)
        t2 = time.time()
        fib_bottom_up(i)
        t3 = time.time()
        topdown.append(t2 - t1)
        bottomup.append(t3 - t2)
        x.append(i+1)
    except:
        pass

    # 12hr * 60min/hr * 60s/min = 43200s
    if time.time() - t0 >= 43200:
        print('maximum value of n: {}'.format(i))
        break

plt.plot(x, topdown, 'r', label='Top Down')
plt.plot(x, bottomup, 'b', label='Bottom Up')
plt.title('TopDown & BottomUp',fontsize=12)
plt.xlabel('n')  
plt.ylabel('time(s)')
plt.legend(loc='upper right')
plt.show()


#Q2
def CountFib4(n):
    # 求f(n-3)
    return fib_bottom_up(n-3)

    
countlist = [ 0 for i in range(5, 51) ]
x = [ i for i in range(5, 51) ]

for i in range(5, 51):

    countlist[i-5] = CountFib4(i)


plt.plot(x, countlist, 'r-o')
plt.title('The times are F(4) computed',fontsize=12)
plt.xlabel('n')  
plt.ylabel('count')
plt.show()