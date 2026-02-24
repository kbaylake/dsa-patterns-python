#Date: 24-02-2026
#771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsCount=Counter(jewels)
        stonesCount=Counter(stones)
        ans=0
        for i in stonesCount:
            if i in jewelsCount:
                ans+=stonesCount[i]
        return ans