from typing import List
from collections import defaultdict
import collections
class Solution1:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hash_map = defaultdict(int)
        count = 0
        for i in chars:
            hash_map[i] += 1
        
        for word in words:
            temp_map = hash_map.copy()
            found = True
            for char in word:
                if char in temp_map and temp_map[char] > 0:
                    temp_map[char] -= 1
                else:
                    found = False
                    break
            if found == True:
                count += len(word)
        return count

print("\nSolution 1.....")
print(Solution1().countCharacters(["cat","bt","hat","tree"], "atach"))
print(Solution1().countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
