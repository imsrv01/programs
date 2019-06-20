'''
find largest number in a array
'''

def largest(arr, size):
    max = arr[0]
    
    for i in range(1,size):
        if arr[i] > max:
            max = arr[i]
    
    return max
    

arr = [1,7,47,5,33]
size = len(arr)
max = largest(arr, size)

print("Largest number in array is " , max)
