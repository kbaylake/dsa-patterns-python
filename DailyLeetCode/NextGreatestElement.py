#Date: 12-03-2026
#496. Next Greatest Element 1
from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dc={}
        for i in range(len(nums2)):
            while stack and  nums2[i]>stack[-1]:
                dc[stack.pop()]=nums2[i]
            stack.append(nums2[i])
        return [dict.get(i, -1) for i in nums1]
            