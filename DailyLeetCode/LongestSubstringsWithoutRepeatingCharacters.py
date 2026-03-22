#3. Longest Substring Without Repeating Characters
#22-03-2026
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        map=set({})
        ans=1
        left=0
        for right in range(len(s)):
            if map and s[right] in map:
                while s[left]!=s[right]:
                    map.remove(s[left])
                    left+=1  
                left+=1
            print(s[left:right+1])
            map.add(s[right])
            ans=max(ans,right-left+1)
        return ans