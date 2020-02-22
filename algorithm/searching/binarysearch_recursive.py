def binarySearch(nums, low, high, target):
    if high >= low: 
        # find the pivot
        middle = int((low + high)//2)
            
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            index = binarySearch(nums,middle+1, high,target)
        else:
            index = binarySearch(nums,low, middle-1, target)
        return index
    else:
        return -1

if __name__ == '__main__':
    nums = [1,4,6,7,8,9]
    print(binarySearch(nums, 0, len(nums)-1, 10))
