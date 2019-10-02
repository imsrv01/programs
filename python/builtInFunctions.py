
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

