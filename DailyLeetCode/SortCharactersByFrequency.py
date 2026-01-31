# Date: 31-01-2026
#92. Sort Characters by Frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        ss=set(s)
        op=[i*s.count(i) for i in ss]
        op=sorted(op,key=len,reverse=True)
        return ''.join(op)
        