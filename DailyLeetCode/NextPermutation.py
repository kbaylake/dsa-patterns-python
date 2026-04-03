class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        right=len(nums)-1
        while right>=0:
            if right+1<len(nums) and nums[right]<nums[right+1]:
                j=len(nums)-1
                while j>right:
                    if nums[j]>nums[right]:
                        break
                    j-=1
                nums[right],nums[j]=nums[j],nums[right]
                nums[right+1:]=nums[right+1:][::-1]
                return
            right-=1
        nums[:]=nums[::-1]
        return