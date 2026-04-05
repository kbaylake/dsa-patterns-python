# 242. Valid Anagram
# 05-04-2026
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=Counter(s)
        s2=Counter(t)
        return s1==s2 