# 347. Top K frequent elemtns
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]