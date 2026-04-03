class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        targets=[]
        def getTarget(nums,target,j):
            left=j+1
            right=len(nums)-1
            res=[]
            while left<right:
                sum=nums[left]+nums[right]
                if sum<target:
                    left+=1
                elif sum>target:
                    right-=1 
                else:
                    res.append([-target,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
            return res
        for j in range(len(nums)):
            if j>0 and nums[j]==nums[j-1]:
                continue
            target=-nums[j]
            curr=getTarget(nums,target,j)
            if curr:
                ans.extend(curr)
        return ans