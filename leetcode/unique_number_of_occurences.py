from typing import List
from collections import defaultdict
import collections
class Solution1:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = defaultdict(int)
        s = set()
        for i in arr:
            hash_map[i] += 1
        for j in hash_map.values():
            if j in s:
                return False
            else:
                s.add(j)
        return True

print("\nSolution 1.....")
print(Solution1().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution1().uniqueOccurrences([1,2]))


# Shorter version using collection..
# Dict subclass for counting hashable items. Sometimes called a bag or multiset. 
# Elements are stored as dictionary keys and their counts are stored as dictionary values.
class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))

print("\nSolution 2.....")
print(Solution2().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution2().uniqueOccurrences([1,2]))