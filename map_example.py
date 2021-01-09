
num = [1, 2, 3, 4]

new_num = map(lambda x: x*2, num) # returns a generator

print(next(new_num))
print(list(new_num))

new_num1 = (i*2 for i in num) # returns a generator
print(list(new_num1))

new_num2 = [i*2 for i in num] # returns a list
print(new_num2)