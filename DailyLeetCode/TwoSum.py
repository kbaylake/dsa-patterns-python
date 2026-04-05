# 1. Two Sum
# 05-04-2026
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc={}
        for i in range(len(nums)):
            tmp=target-nums[i]
            if tmp in dc:
                return [dc[tmp],i]
            else:
                dc[nums[i]]=i