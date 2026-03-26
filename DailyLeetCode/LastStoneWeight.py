#1046 Last Stone Weight
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) # turns an array into a heap in linear time
        while len(stones) > 1:
            largest=abs(heapq.heappop(stones))
            secondLargest=abs(heapq.heappop(stones))
            if largest!=secondLargest:
                heapq.heappush(stones,-abs(largest-secondLargest))
        return -stones[0] if stones else 0
