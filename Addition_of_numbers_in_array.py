'''
Sum of numbers in a array
'''

# Solution 1
def arraySum(arr, size):
    sum = arr[0]
    
    for i in range(1,size):
        sum += arr[i]
    
    return sum
    

arr = [1,7,47,5,33]
size = len(arr)
sum = arraySum(arr, size)

print("Sum of array is " , sum)


# Solution 2
def arraySum(arr, size):
    
    return (sum(arr))  #inbuilt sum function.
