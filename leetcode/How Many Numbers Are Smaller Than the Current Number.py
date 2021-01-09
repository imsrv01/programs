from typing import List
from collections import defaultdict
import collections
class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        temp.sort()
        result = [0]
        hash_map = defaultdict(int)
        for i in range(1, len(temp) ):
            if temp[i] == temp[i-1]:
                result.append(result[i-1])
                hash_map[temp[i]] = result[i-1]
            else:
                result.append(i)
                hash_map[temp[i]] = i
        result.clear()
        for num in nums:
            result.append(hash_map[num])
        return result

print("\nSolution 1.....")
print(Solution1().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution1().smallerNumbersThanCurrent([6,5,4,8]))


from typing import List
from collections import defaultdict
import collections
class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        return [count[num] for num in nums]
        
print("\nSolution 2.....")
print(Solution2().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution2().smallerNumbersThanCurrent([6,5,4,8]))