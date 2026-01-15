# Date: 15-01-2026
# 844. Back Space String Compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            st=[]
            for i in s:
                if i!='#':
                    st.append(i)
                elif st:
                        st.pop()
            return st
        return backspace(s)==backspace(t)