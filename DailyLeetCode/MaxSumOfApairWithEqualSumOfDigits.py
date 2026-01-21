# Date: 21-01-2026
# LeetCode: 2342. Max SumOf A pair With Equal Sum Of Digits
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num):
            sum=0
            while num:
                sum+=num%10
                num//=10
            return sum
        dc=defaultdict(int)
        ans=-1
        for num in nums:
            key=digitSum(num)
            if key in dc:
                ans=max(ans,dc[key]+num)
            dc[key]=max(dc[key],num)
        
        return ans