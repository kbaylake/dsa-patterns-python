# Date: 19-01-2026
# LeetCode: 34. Find the first and last position of element in sorted array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getMid(low,high):
            return (low+high)//2
        def bsLow(nums,val):
            low=0 
            high=len(nums)-1
            while low<high:
                mid=getMid(low,high)
                if nums[mid]>=val:
                    high=mid
                else:
                    low=mid+1
            return low if nums[low]==val else -1
        def bsHigh(nums,val):
            low=0
            high=len(nums)
            while low<high:
                mid=getMid(low,high)
                if nums[mid]>val:
                    high=mid
                else:
                    low=mid+1
            return low-1 if nums[low-1]==val else -1
        if len(nums)==1:
            print('here')
            return [0,0] if target==nums[0] else [-1,-1]
        if not nums:
            return [-1,-1]
        return [bsLow(nums,target),bsHigh(nums,target)]