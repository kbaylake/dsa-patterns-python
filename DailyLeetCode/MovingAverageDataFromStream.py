#Moving Data From Stream
```
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue=deque()
        self.max=size
        self.total=0

    def next(self, val: int) -> float:
        self.total+=val
        self.queue.append(val)
        if len(self.queue)>self.max:
            a=self.queue.popleft()
            print(a)
            self.total-=a
        return self.total/len(self.queue)
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)