#10-3-2026
#1544. Make the string great
import string
class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        dc={char:char.upper() for char in string.ascii_lowercase}
        dc.update({c.upper(): c for c in string.ascii_lowercase})
        for i in s:
            if stack and dc[stack[-1]]==i:
                stack.pop()
                continue
            stack.append(i)
        return ''.join(stack)