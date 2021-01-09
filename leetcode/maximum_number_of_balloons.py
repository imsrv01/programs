#from typing import str
from collections import defaultdict
import collections
class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = defaultdict(int)
        max_count = 0
        not_found = False
        for i in text:
            hash_map[i] += 1
        
        while not_found == False:
            for i in "balloon":
                if i in hash_map and hash_map[i] > 0:
                    hash_map[i] -= 1
                else:
                    not_found = True
                    break
            if not_found == False:
                max_count += 1
        return max_count

print("\nSolution 1.....")
print(Solution1().maxNumberOfBalloons("nlaebolko"))
print(Solution1().maxNumberOfBalloons("loonbalxballpoon"))

class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        return min([cnt[c] // cntBalloon[c] for c in cntBalloon])

print("\nSolution 2.....")
print(Solution2().maxNumberOfBalloons("nlaebolko"))
print(Solution2().maxNumberOfBalloons("loonbalxballpoon"))

