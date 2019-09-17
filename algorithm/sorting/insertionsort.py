list=[48,5,2,12,1,23,17,7]
print("Initial list - ", list)

for i in range(1, len(list)):
    value = list[i]
    hole = i
    while hole > 0 and list[hole-1] > value:
        list[hole] = list[hole-1]
        hole = hole - 1
    list[hole] = value
    
print("Sorted list - ", list)
