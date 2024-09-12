import numpy as np
import matplotlib.pyplot as plt
from random import uniform


train_classes = {
    (-1,6):1,
    (1,1):1,
    (2,0):2,
    (-1,9):2,
   # (1,-2):2,
    
}

test = [(-1,6),(1,1),(2,0),(-1,9)]

def coefs(x1:tuple):
    return 1, 4*x1[0], 4*x1[1], 16*x1[0]*x1[1]

def K(a,b,c,d):   
    def res(x: tuple):
        return a + b*x[0] +c*x[1] + d*x[0]*x[1]
    return res

def p(x:tuple,k):
    if (train_classes.get(x)==1) and  k<=0:
        return 1
    elif (train_classes.get(x)==2) and k>0:
        return -1
    else:
        return 0


def decisive(a,b,c,d):
    def reload_func(x):
        return (-a-b*x)/(d*x+c)
    return reload_func


def visual(func0,bias,funcMain):
    x1 = np.linspace(-10, bias, 50)
    y1 = [func0(i) for i in x1]

    x2 = np.linspace(bias, 10, 50)
    y2 = [func0(i) for i in x2]

    
    for i in range(250):
        x = uniform(-10, 10)
        y = uniform(y2[1], y1[-2])
        if (y < funcMain((x,y))):
            plt.scatter(x, y, color='g')
        else:
            plt.scatter(x, y, color='black')

    plt.plot(x1, y1, color='blue')
    plt.plot(x2, y2, color='blue')
    plt.title('РЕЗУЛЬТАТ')
    plt.ylabel('Значение')
    plt.grid(True)
    plt.show()  


def potential_method():
    i=0
    a=b=c=d=0
    P=1
    while (P!=0) and i+1<len(test):
        t = coefs(test[i])
        a += P*t[0]
        b += P*t[1]
        c += P*t[2]
        d += P*t[3]

        print(a,b,c,d)
        res = K(a,b,c,d)
        y = res(test[i+1])
        P = p(test[i+1],y)
        i+=1

    visual(decisive(a,b,c,d),-c/d,res)


potential_method()        