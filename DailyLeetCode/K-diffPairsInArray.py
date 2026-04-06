#532. K diff Pairs in Array
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        st=Counter(nums)
        ans=0
        if k==0:
            for i in st:
                if st[i]>1:
                    ans+=1
            return ans
        for i in st:
            if i+k in st and st[i+k]>0:
                ans+=1
            if i-k in st  and st[i-k]>0:
                ans+=1
            if i+k in st or i-k in st:
                st[i]=0
        print(st)
        return ans