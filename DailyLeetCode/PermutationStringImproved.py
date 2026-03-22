#567. Permutation String Improved
#567 Permutation String
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1=Counter(s1)
        left=0
        right=len(s1)
        set2=Counter(s2[left:right])
        if set1==set2:
            return True
        for right in range(right,len(s2)):
            set2[s2[left]]-=1
            if set2[s2[left]]==0:
                del set2[s2[left]]
            set2[s2[right]]+=1
            if set2==set1:
                return True
            left+=1
        return False