#567 Permutation String
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1=Counter(s1)
        left=0
        right=len(s1)
        for right in range(right,len(s2)+1):
            curr=s2[left:right]
            set2=Counter(curr)
            if set2==set1:
                return True
            left+=1
        return False