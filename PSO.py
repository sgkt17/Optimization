import random
import numpy as np
import matplotlib.pyplot as plt


def con1(x1):

    if x1 < 10 and x1 > 0.05:

        temp = 0

    else:

        temp = 1
        
    return temp

def con2(x2):

    if x2 < 10 and x2 > 0.05:

        temp = 0

    else:

        temp = 1
    
    return temp
    
def costfunc(arr):

    x1, x2 = arr[0], arr[1]
    
    temp = 50 / ((x1-5)*(x1-5) + (x2-3)*(x2-3) + 25 + 10000000*con1(x1) + 10000000*con2(x2))
    
    return temp
    
def get_initail():

    init_pop = []

    for i in range(iteration):

         x1 = 0.05 + random.random()*(9.95)
         x2 = 0.05 + random.random()*(9.95)

         init_pop.append([x1,x2])

    return init_pop
    
def find_gbest(pop):

    cost = []

    maxv = 0
    maxloc = 0
    
    for i in range(len(pop)):

        temp = costfunc(pop[i])

        cost.append(temp)
        
        if temp > maxv:

            maxv = temp
            maxloc = i

    return maxv, maxloc, cost

def find_pbest(pop, pbest):

    new_pbest = []
    
    for i in range(iteration):
        
        if costfunc(pbest[i]) > costfunc(pop[i]):

            new_pbest.append(pbest[i])

        else :

            new_pbest.append(pop[i])
    
    return new_pbest

def modloc(pop, v, pbest, w):

    v_ = v
    
    maxv, maxloc, cost = find_gbest(pop)
    
    for i in range(iteration):

        for j in range(2):
            
            v_[i][j] = w*v[i][j] + 2*random.random()*(pbest[i][j] -pop[i][j]) + 2*(random.random())*(pop[maxloc][j] - pop[i][j])
    
            pop[i][j] = pop[i][j] + v_[i][j]

    pbest = find_pbest(pop, pbest)

    w = 0.95*w
    return pop, v_, pbest, w
        
if __name__ == "__main__":

    global iteration

    iteration = 50
    
    w = 0.8
    
    pop = get_initail()

    pbest = pop
    
    v = [[random.uniform(-0.1,0.1)*pop[i][0],random.uniform(-0.1,0.1)*pop[i][1]] for i in range(50)]

    for i in range(50):
        
        pop, v, pbest, w = modloc(pop, v, pbest, w)

        pop = np.array(pop)

        pop = pop.transpose()

        plt.scatter(pop[0],pop[1])

        plt.xlim(-2, 9)
        plt.ylim(-2, 9)
        plt.title("iteration = " + str(i) )
            
        plt.show()

        pop = pop.transpose()
    
        maxv, maxloc, cost = find_gbest(pop)
