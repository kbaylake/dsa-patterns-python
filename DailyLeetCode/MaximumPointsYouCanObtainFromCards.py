#03-03-2026
#1423. Maximum Points you can obtain from cards solved
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        right=-1
        if k==len(cardPoints):
            return sum(cardPoints)
        left=k-1
        ans=curr=sum(cardPoints[0:k])
        while left>=0:
            curr=curr-cardPoints[left]+cardPoints[right]
            ans=max(ans,curr)
            left-=1
            right-=1
        return ans