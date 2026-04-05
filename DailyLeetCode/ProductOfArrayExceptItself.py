# 238. Product of array except itself
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        right=len(nums)-1
        for i in range(len(nums)):
            if i==0:
                prefix.append(nums[i])
                continue
            prefix.append(prefix[i-1]*nums[i])
        while right>=0:
            if right==len(nums)-1:
                postfix.append(nums[right])
                right-=1
                continue
            postfix.append(postfix[-1]*nums[right]) 
            right-=1
        postfix=postfix[::-1]
        ans =[]
        for i in range(len(nums)):
            if i==0:
                ans.append(postfix[i+1])
                continue
            if i==len(nums)-1:
                ans.append(prefix[i-1])
                continue
            ans.append(prefix[i-1]*postfix[i+1])
        return ans