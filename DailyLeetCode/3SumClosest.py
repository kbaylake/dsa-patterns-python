# 16. 3Sum Closest 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff=float('inf')
        ans=None
        def twoSum(nums,target,i):
            minDiff=float('inf')
            tmp=None
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[left]+nums[right]
                absDiff=abs(target-total)
                if absDiff<minDiff:
                    minDiff=absDiff
                    tmp=total+nums[i]
                if total>target:
                    right-=1
                else:
                    left+=1
            return minDiff,tmp
        for i in range(len(nums)):
            t=target-nums[i]
            tmpDiff,tmpAns=twoSum(nums,t,i)
            if tmpDiff<minDiff:
                minDiff=tmpDiff
                ans=tmpAns
        return ans
    
## Improved
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff=float('inf')
        ans=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            t=target-nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[left]+nums[right]
                absDiff=abs(t-total)
                if absDiff<minDiff:
                    minDiff=absDiff
                    ans=total+nums[i]
                if total>t:
                    right-=1
                else:
                    left+=1
        return ans