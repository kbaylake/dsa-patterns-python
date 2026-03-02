#number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        right=left+k
        ans=0
        thresh=threshold*k
        windowSum=sum(arr[left:right])#[0:3] [2,2,2]
        if windowSum>=thresh:
            ans+=1
        for right in range(right,len(arr)):
            windowSum=windowSum-arr[left]+arr[right]
            if windowSum>=thresh:
                ans+=1
            left+=1
        return ans