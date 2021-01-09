#Approach #1 ( hashtable)
# Time complexity - O(n) - 
# Space complexity - O(n) - extra memory is used, computation is done on the hash table
from typing import List
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True

print("\nSolution 1.....")
print(Solution1().isIsomorphic("egg", "add"))
print(Solution1().isIsomorphic("foo", "bar"))                                           
