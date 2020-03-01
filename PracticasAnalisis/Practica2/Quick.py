import random 
import timeit

def quicksort(arr, start, stop): 
    if(start < stop): 
          
        # pivotindex is the index where 
        # the pivot lies in the array 
        pivotindex = partitionrand(arr, start, stop) 
          
        # At this stage the array is partially sorted  
        # around the pivot. separately sorting the  
        # left half of the array and the right half of the array. 
        quicksort(arr , start , pivotindex) 
        quicksort(arr, pivotindex + 1, stop) 
  
# This function generates random pivot, swaps the first 
# element with the pivot and calls the partition function. 
def partitionrand(arr , start, stop): 
    randpivot = random.randrange(start, stop) 
    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
    return partition(arr, start, stop) 
  

def partition(arr,start,stop): 
    pivot = start # pivot 
    i = start - 1
    j = stop + 1
    while True: 
        while True: 
            i = i + 1
            if arr[i] >= arr[pivot]: 
                break
        while True: 
            j = j - 1
            if arr[j] <= arr[pivot]: 
                break
        if i >= j: 
            return j 
        arr[i] , arr[j] = arr[j] , arr[i] 

best_case = []
worst_case = []
rand_case = []
for i in range(10):
    f = open('best_case/b_' + str(i+1) + "000", 'r')
    x = f.read().split()
    best_case.append(x)
    f.close()

for i in range(10):
    f = open('rand_case/rand_' + str(i+1) + "000", 'r')
    x = f.read().split()
    rand_case.append(x)
    f.close()

for i in range(10):
    f = open('worst_case/w_' + str(i+1) + "000", 'r')
    x = f.read().split()
    worst_case.append(x)
    f.close()


f= open("data","w+")
for i in range(10):
    start= 0
    end = 0
    start = timeit.timeit()
    quicksort(best_case[i],0, len(best_case[i])-1 )
    end = timeit.timeit()
    f.write(str(end) +  ", ")
    print(end - start)

f.write("\n")

for i in range(10):
    start = timeit.timeit()
    quicksort(worst_case[i],0, len(worst_case[i])-1 )
    end = timeit.timeit()
    f.write(str(end) +  ", ")
    print(end - start)
f.write("\n")

for i in range(10):
    start = timeit.timeit()
    quicksort(rand_case[i],0, len(rand_case[i])-1 )
    end = timeit.timeit()
    f.write(str(end) +  ", ")
    print(end - start)


# array = [10, 7, 8, 9, 1, 5] 
# start = timeit.timeit()
# quicksort(array, 0, len(array) - 1)
# end = timeit.timeit()

# print(array) 

print(end - start)



f.close()

print(end - start)