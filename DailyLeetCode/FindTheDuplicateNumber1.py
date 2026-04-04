#287. Find the duplicate number
#04-04-2026
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        for right in range(1,len(nums)):
            if nums[left]==nums[right]:
                return nums[right]
            left+=1
        return -1
## Improved
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=[False]*len(nums)
        for i in nums:
            if seen[i]:
                return i
            seen[i]=True