from typing import List
from collections import defaultdict
import collections
class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        result = 0
        for i in range(len(nums)):
            num = nums[i]
            if num in hash_map:
                hash_map[num].append(i)
            else:
                temp_list = [i]
                hash_map[num] = temp_list
        
        for val in hash_map.values():
            if len(val) > 1:
                for j in range(len(val), 0, -1):
                    result += j-1 

        return result

print("\nSolution 1.....")
print(Solution1().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution1().numIdenticalPairs([1,1,1,1]))
print(Solution1().numIdenticalPairs([1,2,3]))
