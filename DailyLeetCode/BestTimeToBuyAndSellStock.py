#121 Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if prices[i]<minPrice:
                minPrice=prices[i]
                continue
            ans=max(prices[i]-minPrice,ans)
        return ans