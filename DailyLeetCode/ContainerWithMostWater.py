#11. Container With Most Water 
#22-03-2026
class Solution:
    def maxArea(self, height):
        left=0
        right=len(height)-1
        ans=0
        while left<=right:
            curr=min(height[left],height[right])*(right-left)
            ans=max(ans,curr)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
nums=[-1,0,1,2,-1,-4]
nums.sort()
print(nums)