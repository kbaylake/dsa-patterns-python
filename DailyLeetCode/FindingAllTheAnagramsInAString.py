#02-03-26
#438. Finding all the anagrams in a string
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        right=len(p)
        dc=Counter(p)#Dictionary for p
        windowDict=Counter(s[left:right])#Starting Window Dictionary
        ans=[]
        if windowDict==dc:
            ans.append(0)
        for right in range(right,len(s)):
            windowDict[s[left]]-=1
            windowDict[s[right]]+=1
            left+=1
            if windowDict==dc:
                ans.append(left)
        return ans