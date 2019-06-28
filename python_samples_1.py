
#### Length
str="hello"
print("Length of str - ", len(str))

arr = [1,2,3,4,5]
print("Length of array - ", len(arr))

#Range range(start, stop, step) - all are integers..
for i in range(6):
  print(i)
  
for i in range(1,6):
  print(i)
  
for i in range(1,6,2):
  print(i)
  
#### PARSE
arr = [1,2,3,4,5]
print("Reversed array - ", arr[::-1])
print("first 2 elements of array - ", arr[0:2:])

str = "hello"
print("Reversed string - ", str[::-1])
print("substring - ", str[1:3:])

#### REVERSE
o	testList.reverse() # inplace reverse, no copy is created, do not return new list.
o	testList[::-1]   # slicing method
o	list(reversed(testList)) # returns iterator and converted to list


