# 238. Product of array except itself
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        postfix=1
        right=len(nums)-1
        ans =[]
        for i in range(len(nums)):
            if i==0:
                prefix=1
            else:
                prefix=prefix*nums[i-1]
            ans.append(prefix)
        while right>=0:
            if right==len(nums)-1:
                postfix=1
            else:
                postfix=postfix*nums[right+1]
            ans[right]=ans[right]*postfix
            right-=1
        return ans