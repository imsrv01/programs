'''
Given a string, write a Python program to split the characters of the given string into a list.

Examples:

Input : geeks
Output : ['g', 'e', 'e', 'k', 's']

Input : Word
Output : ['W', 'o', 'r', 'd']

'''

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
