
def test_fn_generator():
    yield 1
    yield 2
    yield 3

class test_class_generator:
    def __init__(self):
        self.num = 0

    def __next__(self):
        self.num += 1
        return self.num

    def __iter__(self):
        return self

# funtion generator test
print('function generator test....')
g = test_fn_generator()
print(g)
print(next(g))

# class generator test
cg = test_class_generator()
print(next(cg))

for i in test_class_generator():
    if i < 10:
        print(i)