# 128. Longest Consecutive Subsequence
from collections import deque
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        ans=0
        for i in st:
            cnt=1
            if i-1 not in st:
                while i+1 in st:
                    i+=1
                    cnt+=1
                ans=max(ans,cnt)
        return ans