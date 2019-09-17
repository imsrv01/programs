list = [5,2,12,1,23,17]
#list=[1, 2, 5, 12, 17, 23]
print('Initial List : -',list)
swapped=False
for i in range(len(list)-1):
  for j in range(len(list)-i-1):
    if list[j] > list[j+1]:
      (list[j], list[j+1]) = (list[j+1], list[j])
      swapped = True
  if(swapped == False):
    print('List already sorted')    
    break
print('Sorted List : -',list)
