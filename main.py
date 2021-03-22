from random import randint
import time

sel = []

#Generate Matrix
for i in range (500):
    temp = []
    for j in range (500):
        temp.append(randint(0, 500))
    sel.append(temp)
quick = sel
sort = sel
#Selection Sort
def selectionSort(array):
    for i in range(len(array) - 1):
        min = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min]:
                min = j
            j = j + 1
        array[i], array[min] = array[min], array[i]
def selectionSortMatrix(matrix):
    for row in matrix:
        selectionSort(row)

#Quicksort
def divide(arr, low, high):
    i = (low - 1)
    piv = arr[high]
    for j in range(low, high):
        if arr[j] <= piv:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = divide(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
def quickSortMatrix(matrix):
    for row in matrix:
        n = len(row)
        quickSort(row, 0, n-1)

#Sort
def sortMatrix(matrix):
    for row in matrix:
        row.sort()

#Print Matrix
def printMatrix(matrix):
    for row in matrix:
        print(row)
        print('\n')

#Test
print("quickSort started...")
start = time.time()
quickSortMatrix(quick)
end = time.time()
print("finished in: " + str(end-start) + " sec." + '\n')
print("selectionSort started... ")
start = time.time()
selectionSortMatrix(sel)
end = time.time()
print("finished in " + str(end-start) + " sec." + '\n')
print("defaultSort started... ")
start = time.time()
sortMatrix(sort)
end = time.time()
print("finished in " + str(end-start) + " sec." + '\n')