#387. First Unique Character in string
#05-04-2026
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dc=Counter(s)
        for i in range(len(s)):
            if dc[s[i]]==1:
                return i
        return -1