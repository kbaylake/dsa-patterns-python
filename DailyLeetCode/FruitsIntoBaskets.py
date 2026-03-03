#904 Fruits into baskets
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=right=ans=0
        st=defaultdict(int)
        for right in range(len(fruits)):
            st[fruits[right]]+=1
            while len(st)>2:
                curr=fruits[left]
                st[curr]-=1
                if st[curr]==0:
                    st.pop(curr)
                left+=1
            if len(st)<=2:
                ans=max(ans,right-left+1)
        return ans