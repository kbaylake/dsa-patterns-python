#02-03-2026
#Minimum size of sub array
import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum=0
        ans=math.inf
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                ans=min(ans,right-left+1)
                sum-=nums[left]
                left+=1
        return 0 if ans==math.inf else ans