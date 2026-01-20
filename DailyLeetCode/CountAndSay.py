# Date: 20-01-2026
# LeetCode: 38. Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        return Solution.rle(Solution.countAndSay(self,n-1))
    def rle(n: int):
        n=str(n)#Space O(n)
        op=''
        i=0
        while i <len(n):#Time O(n)
            count=1
            j=i+1
            while j <len(n) and n[i]==n[j]:
                count+=1
                j+=1
            temp=str(count)+n[i]
            op+=temp
            i=j
        return op
        