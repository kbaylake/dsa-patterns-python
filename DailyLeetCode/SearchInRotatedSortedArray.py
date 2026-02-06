# Date: 04-02-2026
#33. Search in a rotated sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMax(nums):
            low=0
            high=len(nums)-1
            if nums[low]<=nums[high]:
                return high
            while low<high:
                mid=(low+high)//2
                if nums[mid]>nums[high]:
                    low=mid+1
                else:
                    high=mid
            return low-1
        max_index=findMax(nums)
        low=0
        high=len(nums)-1
        if target==nums[max_index]:
            return max_index
        if target<nums[low]:
            low=max_index+1
        elif target<nums[max_index]:
            high=max_index-1
        def getMid(low,high):
            return (low+high)//2
        def binarySearch(arr,val,low,high):
            mid=getMid(low,high)
            while arr[mid]!=val:
                if arr[mid]<val:
                    low=mid+1
                else:
                    high = mid-1
                if low>high:
                    return -1
                mid=getMid(low,high)
            return mid
        return binarySearch(nums,target,low,high)
