import random
import numpy as np

def val(chrosome):

    x = decoding(chrosome)
    
    obj = x*x + 10000 
    
    return obj

def decoding(chrosome):

    x = int(chrosome, 2)

    return x

def Parents():

    chromosome = []

    for i in range(40):
        n = random.randrange(0,32)
        temp = "{0:b}".format(n).zfill(5)
        chromosome.append(temp)

    return chromosome
    

def Rollte(chromosome):

    total = sum([val(i) for i in chromosome])
    selection = [val(i)/total for i in chromosome]
    newchromosome = []
    
    for i in range(40):
        newchromosome.append(np.random.choice(chromosome, p=selection))

    return newchromosome


def Crossover(chromosome):
    
    total = sum([val(i) for i in chromosome])
    selection = [val(i)/total for i in chromosome]
    newchromosome = []
    
    for i in range(0,40,2):
        
        n = random.randrange(0,6)

        newchromosome.append(chromosome[i][:n] + chromosome[i+1][n:])
        newchromosome.append(chromosome[i+1][:n] + chromosome[i][n:])
        
    return newchromosome

if __name__ == "__main__":

    chromosome = Parents()
    print("total fitness value: " + str(sum([val(i) for i in chromosome])))
    
    for i in range(100):
        
        temp = Rollte(chromosome)
        new_chromosome = Crossover(temp)
        chromosome = new_chromosome
        print("total fitness value: " + str(sum([val(i) for i in chromosome])))
              
    print(chromosome)
