## 18 4sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        op=[]
        def twoSum(nums,target,k,a,b):
            left=k
            right=len(nums)-1
            tmp=[]
            while left<right:
                total=nums[left]+nums[right]
                if total>target:
                    right-=1
                elif total<target:
                    left+=1
                else:
                    tmp.append([a,b,nums[left],nums[right]])
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
            newTarget=target-nums[i]
            for j in range(i+1,len(nums)):
                tmpTarget=newTarget-nums[j]
                if (j>i+1 and nums[j]==nums[j-1]):
                    continue
                ans=twoSum(nums,tmpTarget,j+1,nums[i],nums[j])
                if ans:
                    op.extend(ans)
        return op