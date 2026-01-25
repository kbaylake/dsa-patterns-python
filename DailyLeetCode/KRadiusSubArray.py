# Date: 25-01-2026
# 2090: K Radius Sub Arrays
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixes=[nums[0]]
        for i in range(1,len(nums)):
            prefixes.append(nums[i]+prefixes[-1])
        ans=[]
        n=len(nums)
        for i in range(n):
            if i-k>=0 and i+k<n:
                ans.append((prefixes[i+k]-prefixes[i-k]+nums[i-k])//(2*k+1))
            else:
                ans.append(-1)
        return ans