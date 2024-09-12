import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
import random

def draw_result(linkage_matrix):
    dendrogram(linkage_matrix)
    plt.show()


SIZE = random.randint(4,30)
table_d = [[0 for i in range(SIZE)] for i in range(SIZE)]





def generate():
    for i in range(SIZE):
        for j in range(i):
            table_d[i][j] = random.randint(2, 105)
            table_d[j][i] = table_d [i][j]

generate()            



def reverse():
    for i in range(len(table_d)):
        for j in range(i):
            table_d[i][j] = 1/table_d[i][j] 
            table_d[j][i] = table_d [i][j]



def store_groups(new_group:tuple[int]):
    print(new_group)
    table_d.append([0 for i in table_d[0]])
    for i in table_d:
        i.append(0)

    for i in range(len(table_d[0])):
        if not (i in new_group):

            tmp = min(table_d[new_group[0]][i],table_d[new_group[1]][i])
            
            table_d[-1][i] = tmp
            table_d[i][-1] = tmp

    for i in range(len(table_d[0])):
        table_d[new_group[0]][i] = 0
        table_d[new_group[1]][i] = 0
        table_d[i][new_group[1]] = 0
        table_d[i][new_group[0]] = 0
    




def maximum():
    min1 = 0
    saveI=saveJ=0
    for i in range(len(table_d)):
        for j in range(i+1,len(table_d[0])):    
                if table_d[i][j]>0 and min1<table_d[i][j]:
                    min1 =table_d[i][j]
                    saveI = i
                    saveJ = j              
    return saveI,saveJ,min1



def minimum():
    min1 = np.inf
    saveI=saveJ=0
    for i in range(len(table_d)):
        for j in range(i+1,len(table_d[0])):    
                if table_d[i][j]>0 and min1>table_d[i][j]:
                    min1 =table_d[i][j]
                    saveI = i
                    saveJ = j              
    return saveI,saveJ,min1


def printT():
    for i in table_d:
        print(i)        
    print()    

def mins(): 
    min1 = 0
    result =[]
    printT()
    while min1!=np.inf:
        i,j,min1 = minimum()
        if i or j:
            result.append([i,j,float(min1),0])
            store_groups((i,j))  
    print(result)
    draw_result(result)


def maxs():
        min1 = 1
        result =[]
        printT()
        while min1!=0:
            i,j,min1 = maximum()
            if i or j:
                result.append([i,j,float(min1),0])
                store_groups((i,j))  
        print(result)
        draw_result(result)

        return result

#reverse()

mins()