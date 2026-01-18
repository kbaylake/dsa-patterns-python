# Date: 15-01-2026
# LeetCode: 2958. Length of Longest Subarray With at Most K Frequency
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dc=defaultdict(int)
        ans=left=right=0
        for right in range(len(nums)):
            dc[nums[right]]+=1
            while dc[nums[right]]>k:
                dc[nums[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans