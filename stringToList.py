'''
Given a string, write a Python program to split the characters of the given string into a list.

Examples:

Input : geeks
Output : ['g', 'e', 'e', 'k', 's']

Input : Word
Output : ['W', 'o', 'r', 'd']

'''
# Solution

def splitString(str):
  targetList=[]
  for i in range(len(str)): # Charcters are retrived using string parsing
    character = str[i:i+1:]
    targetList.append(character)
  return targetList

str = "geeks"
arr = splitString(str)
print(arr)

# Solution
def splitString(str):
  targetList=[]
  for i in str: # Characters are retrived using iterator
    targetList.append(i)
  return targetList

str = "geeks"
arr = splitString(str)
print(arr)

# SOLUTION 1

def split(word): 
  return [char for char in word]  
      
word = 'geeks'
print(split(word)) 


# SOLUTION 2

def split(word): 
  return list(word)  
      
word = 'geeks'
print(split(word)) 
