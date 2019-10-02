list1 = [1,2,3,4,5]
list2 = [11,23,33]

# print original list1
print('list1 - ', list1)

# print length
print('list length - ',len(list1))

# get slice
print("Slice 1:3 - ", list1[1:3])

# Add item to the end of list
list1.append(6)
print('After append 6 - ', list1)

# Add item to the end of list
list1.insert(0,0)
print('Insert item at 0th position - ', list1)

# Remove item - pass element, does not return any value
list1.remove(2)
print('Remove item 2 - ', list1)

# Pop item - pass index, return removed item.. Default index -1 , last item
print('POP item - ', list1.pop(2))
print('Modified list - ', list1)
print('POP item - ', list1.pop())
print('Modified list - ', list1)

# Add items from second array
list1.extend(list2)
print('Extend array - ', list1)

# append second array
list1.append(list2)
print('Append second array - ', list1)

# count occurence of item
print('Count - ', list1.count(5))

# reverse
list1.pop()
list1.reverse()
print('reverse', list1) 

# sort
list1.sort()
print('reverse', list1) 

# COPY, returns a new list.. updating new list does not modify org list.. shallow copy
print('shallow copy - ')
list3 = list1.copy()
list3.append(100)
print(list3)
print(list1)

# Another copy way - affect org list when new list updated
print('Regular copy - ')
list4 = list1
list4.append(125)
print(list4)
print(list1)

# Slice copy way - slice creates a new list.. org list does not get affected..
print('Slice copy - ')
list5 = list1[:]
list5.append(130)
print(list5)
print(list1)
 
# Clear list
list1.clear()
print(list1)
