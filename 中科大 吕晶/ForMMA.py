import numpy as np
def riffle(a,b):
    n=np.size(a)
    c=[]
    for i in range(0,n):
        c.append(a[i])
        c.append(b[i])
    return c

def partition(a,n):
    nn=int(np.size(a)/n)
    c=[]
    for i in range(0,nn):
        d=[]
        for j in range(0,n):
            d.append(a[n*i+j])
        c.append(d)
    return c


def map(f,obj):
    n=len(obj)
    c=[]
    for i in range(0,n):
        c.append(f(obj[i]))
    return c
