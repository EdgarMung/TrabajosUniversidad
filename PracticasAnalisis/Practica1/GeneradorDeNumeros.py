import os
import random

def rand_num():
    number = random.randint(0,1000)
    return number

def best(aux):
    for i in range(1,11):
        file_name = "best_case/b_" + str(i) + "000"
        file = open(file_name, "w")
        for j in range(0,aux):
            file.write(str(j)+ "\n")
        file.close()
        aux = aux + 1000
    pass

def worst(aux):
    for i in range(1,11):
        file_name = "worst_case/w_" + str(i) + "000"
        file = open(file_name, "w")
        for j in range(0,aux):
            file.write(str(aux- j)+ "\n")
        file.close()
        aux = aux + 1000
    pass
    

def rand(aux):
    for i in range(1,11):
        file_name = "rand_case/rand_" + str(i) + "000"
        file = open(file_name, "w")
        for j in range(0,aux):
            file.write(str(rand_num()) + "\n")

        file.close()
        aux = aux + 1000
    pass
    
        
directories =["rand_case/", "best_case/", "worst_case/" ]
aux = 1000

for directory in directories:
    try:
        os.mkdir(directory)
    except OSError:
        print ("Directory already created %s" % directory)
    else:
        print ("Successfully created the directory %s" % directory)


best(aux)
worst(aux)
rand(aux)