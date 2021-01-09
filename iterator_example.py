
def iter_example():
    list1 = [1,2,3,4,5]
    iter1 = iter(list1)
    while True:
        try:
            print(next(iter1))
        except StopIteration:
            break

#iter_example()

def first_tennumbers():
    i = 0
    while i < 10:
        i += 1
        yield i # execution of the function is halted here, next run of the function, yield results will be remembered and used in calculation..

for i in first_tennumbers():
    print(i)
