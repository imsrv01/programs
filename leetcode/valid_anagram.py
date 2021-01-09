
#Approach #1 ( hashtable)
# Time complexity - O(n) - 
# Space complexity - O(n) - extra memory is used, computation is done on the hash table
from typing import List
from collections import defaultdict
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = defaultdict(int)
        for i in t:
            hash_map[i] += 1
        for i in s:
            if i in hash_map:
                if hash_map[i] == 1:
                    del hash_map[i]
                else:
                    hash_map[i] -=1
        if len(hash_map) == 0:
            return True
        else:
            return False
print("\nSolution 1.....")
print(Solution1().isAnagram("anagram", "nagaram"))
print(Solution1().isAnagram("rat", "car"))