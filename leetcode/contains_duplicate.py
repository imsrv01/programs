
#Approach #1 (Naive Linear Search)
# Time complexity - O(n2)
# Space complexity - O(1) - No extra memory is used, computation is done on the input list
from typing import List
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] == nums[i]:
                    return True
        return False
print("Solution 1.....")
print(Solution1().containsDuplicate([1,2,3,1]))
print(Solution1().containsDuplicate([1,2,3,4]))

#Approach #2 (Sorting)
# Time complexity - O(nlogn) - sorting takes this time, other operations are constant
# Space complexity - O(1) - No extra memory is used, computation is done on the input list
from typing import List
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1): # why -1 ? next statement is looking for next element, avoid index out of range error..
            if nums[i] == nums[i+1]:
                return True
        return False
print("\nSolution 2.....")
print(Solution2().containsDuplicate([1,2,3,1]))
print(Solution2().containsDuplicate([1,2,3,4]))

#Approach #3 (Set / hashtable)
# Time complexity - O(n) - 
# Space complexity - O(n) - extra memory is used, computation is done on the hash table
from typing import List
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i not in s:
              s.add(i)
            else:
                return True
        return False
print("\nSolution 3.....")
print(Solution3().containsDuplicate([1,2,3,1]))
print(Solution3().containsDuplicate([1,2,3,4]))

# one liner using len function
from typing import List
class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
       return len(set(nums)) < len(nums)
print("\nSolution 4.....")
print(Solution4().containsDuplicate([1,2,3,1]))
print(Solution4().containsDuplicate([1,2,3,4]))