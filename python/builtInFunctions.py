
class Animal:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return 'repr - {}'.format(self.name)
    
    def __str__(self):
        return 'str - {}'.format(self.name)
    
    def __hash__(self):
        return 100
    
    def __equal__(self, other):
        return self.name == other.name
        
class Dog(Animal):
    pass

class Cat:
    pass

list1 = [1,2,3,4,5]
dog1 = Dog("Robert")
dog2 = Dog("Simba")

print(len(list1))
print(repr(dog1))
print(str(dog1))
print(isinstance(dog1, Dog))
print(issubclass(Dog, Animal))
#print(help(Dog))
print(hash(dog1))
print(dog1 == dog2)
#print(dict(dog1))
i = input('Enter you name')
print('your name {}'.format(i))

# The ord() method returns an integer representing Unicode code point for the given Unicode character.
# Input - c - character string of length 1 whose Unicode code point is to be found
# Output - 99
print(ord('c'))

# Inverse of above
# The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
# The valid range of the integer is from 0 through 1,114,111.
# Output - c
print(chr(99))

# Returns type/class of object
# Output - <class 'int'>
a=40
print(type(a))

# The bin() method converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
# Output - 0b1000
print(bin(8))
