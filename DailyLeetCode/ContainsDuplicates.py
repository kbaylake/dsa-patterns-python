# 217. Contains Duplicates
#05-04-2026
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        return len(s)!=len(nums)