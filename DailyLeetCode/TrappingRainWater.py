# 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        maxLeft=[0]*len(height)
        maxRight=[0]*len(height)
        for i in range(1,len(height)):
            maxHeight=max(height[i-1],maxLeft[i-1])
            maxLeft[i]=maxHeight
        for i in range(len(height)-2,0,-1):
            maxHeight=max(height[i+1],maxRight[i+1])
            maxRight[i]=maxHeight
        for i in range(len(height)):
            currHeight=min(maxLeft[i],maxRight[i])
            if currHeight==0:
                continue
            currSum=currHeight-height[i]
            if currSum>0:
                total+=currSum
        return total