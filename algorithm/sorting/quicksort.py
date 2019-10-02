
def quicksort(list, low, high):
    if low < high:
        j = partition(list, low, high)
        quicksort(list,low, j)
        quicksort(list,j+1, high)

def partition(list, low, high):
    pivot = list[low]
    i=low
    j=high

    while i < j:
        while list[i] <= pivot:
            i = i+1
        while list[j] > pivot:
            j = j-1
        if i < j:
            (list[i], list[j]) = (list[j], list[i])
    (list[low], list[j]) = (list[j], pivot)
    return j

list = [32,9,57,45,10, 12 , 39, 11]
quicksort(list, 0, len(list)-1)
print('SORTED list - ', list)
