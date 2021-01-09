from typing import List
from collections import defaultdict
import collections
class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num_set = set()
        for num in arr:
            num_set.add(num)
        
        start = 1
        missing_set = set()
        while len(missing_set) < k:
            if start not in num_set:
                missing_set.add(start)
            start += 1
        return start - 1 

print("\nSolution 1.....")
print(Solution1().findKthPositive([2,3,4,7,11], 5))
print(Solution1().findKthPositive([1,2,3,4],2))


# Timecomplexity - O(logn) - Binary search
# Space - O(1) - No extra space is used..
from typing import List
from collections import defaultdict
import collections
class Solution2:
    def findKthPositive(self, A: List[int], k: int) -> int:
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k

print("\nSolution 2.....")
print(Solution2().findKthPositive([2,3,4,7,11], 5))
print(Solution2().findKthPositive([1,2,3,4],2))