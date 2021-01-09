
def first_tennumbers():
    i = 0
    while i < 10:
        i += 1
        yield i # execution of the function is halted here, next run of the function, yield results will be remembered and used in calculation..

g = first_tennumbers() # returns a generator object
print(g)
print(next(g)) # first run of the function
print(next(g)) # second run of the function.
print(next(first_tennumbers())) # next should be called on same generator object, here it returns 1 instead of 3. Next is called on a new generator object..

for i in first_tennumbers():
    print(i)