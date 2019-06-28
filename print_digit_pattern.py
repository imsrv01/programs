'''
Print digit pattern

Input : 41325
Output :
|****
|*
|***
|**
|*****
Explanation: for a given integer print the number of *’s that are equivalent to each digit in the integer. Here the first digit is 4 so print four *sin the first line. The second digit is 1 so print one *. So on and the last i.e., the fifth digit is 5 hence print five *s in the fifth line.

Input : 60710
Output :
|******
|
|*******
|*
|
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
