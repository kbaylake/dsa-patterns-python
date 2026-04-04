class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        op=[]
        def twoSum(nums,target,j):
            left=j
            right=len(nums)-1
            tmp=[]
            while left<right:
                total=nums[left]+nums[right]
                if total>target:
                    right-=1
                elif total<target:
                    left+=1
                else:
                    tmp.append([-target,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
            return tmp
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            ans=twoSum(nums,target,i+1)
            if ans:
                op.extend(ans)
        return op
            