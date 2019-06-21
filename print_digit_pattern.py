'''
Print digit pattern
'''

#Solution 1
def digitPattern(number, size):
    number = str(number)
    i=0
    while(i < size):
        digit = int(number[i])
        i += 1
        if digit == 0:
            print ("/")
            continue
        if digit == 1:
            print("/*")
            continue
        j=0
        while (j < digit):
            if (j == 0):
                print("/*", end="")
            else:    
                if (j < (digit -1) ):
                    print("*", end="")
                else:
                    print("*")
            j += 1    
        
    
num = 41309025
size = len(str(num))
digitPattern(num, size)

#Solution 2

def digitPattern(number):
    for i in number:
      print("/", end="")
      print("*" * int(i))
      
num = 41309025
digitPattern(str(num))
