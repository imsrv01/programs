



x = lambda x:x*2

list1 = [1,2,3,4,5]
list2 = list(map(lambda x:x*2, list1))
list3 = list(filter(lambda x: x%2 == 0, list1))
list4 = list(filter(lambda x: x%2 != 0, list1))
print(x(2))
print(list2)
print(list3)
print(list4)
print([ 1 for i in list1])

class test:
    a=10
    def __init__(self, b):
        self.b=b

    def display(self):
        #print(self.b)
        print("hello")

    @classmethod
    def show(cls,b):
        return cls(b)

    @staticmethod
    def staticshow():
        print('static method')


test1 = test(15)
print(test1.b)
print(test1.a)
print(test1.display())

test.staticshow()
print(test.show(30).b)



x = "AAAdfdfdsf"
print(x[5])
for i in range(len(x)):
    print(x[i])
