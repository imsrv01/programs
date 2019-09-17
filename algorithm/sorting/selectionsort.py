list=[48,5,2,12,1,23,17,7]

print("Initial list - ", list)

for i in range(len(list)-1): # last element will already be in its correct position.. hence n-1 elements will need to be brought to correct positions..

  min = i # consider the fist element as minimum

  for j in range(i+1,len(list)): # Comparison will be done against the next number in array..

    if list[j] < list[min]: # if next element is smaller than the original minimum, make it the minimum..

      min = j

  temp = list[i]

  list[i]=list[min] # at the end of each loop, we have found the minimum element, place it at correct position,,

  list[min]=temp 

print("Sorted list - ", list)
