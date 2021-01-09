
#Approach #1 ( hashtable)
# Time complexity - O(n) - 
# Space complexity - O(n) - extra memory is used, computation is done on the hash table
from typing import List
class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                if (i - hash_map[nums[i]]) <= k:
                    return True
                else:
                    hash_map[nums[i]] = i
        return False
print("\nSolution 1.....")
print(Solution1().containsNearbyDuplicate([1,2,3,1], 3))
print(Solution1().containsNearbyDuplicate([1,2,3,1,2,3], 2))

# Shorter version using enumerate function
from typing import List
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
print("\nSolution 2.....")
print(Solution2().containsNearbyDuplicate([1,2,3,1], 3))
print(Solution2().containsNearbyDuplicate([1,2,3,1,2,3], 2))
