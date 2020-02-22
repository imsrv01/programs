def binarySearch(nums, low, high, target):
    # only if high is greaterthan or equal to low
    if high >= low: 
        # find the pivot
        middle = int((low + high)//2)
        
        # check if pivot element is equal to target element, return pivot index if tue    
        if nums[middle] == target:
            return middle
        # if pivot is lesser than target, call binary search on right side of array
        # low = middle+1 
        if nums[middle] < target:
            # Accept the returned index
            index = binarySearch(nums,middle+1, high,target)
        else:
            # if pivot is greater than target, call binary search on left side of array
            # high = middle-1
            index = binarySearch(nums,low, middle-1, target)
        return index
    else:
        # return -1 if not found
        return -1
