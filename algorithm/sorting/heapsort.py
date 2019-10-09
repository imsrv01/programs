# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    print('heapify', arr, n , i)
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        print('swapping', arr[i], arr[largest])
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap. output will be just a max heap....
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    print('extract elements')
    # One by one extract elements
    # start with list end element (n-1), and do this till second last element 1, notice 0 - it is not included...
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

# Driver code to test above
arr = [ 26, 11, 5, 53, 1, 7,9]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
# This code is contributed by Mohit Kumra
