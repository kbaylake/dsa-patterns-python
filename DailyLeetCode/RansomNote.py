class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount=Counter(ransomNote)
        magazineCount=Counter(magazine)
        ans=set()
        for i in ransomCount:
            if i in magazineCount and magazineCount[i]>=ransomCount[i]:
                ans.add(True)
            else:
                ans.add(False)
        return False if False in ans else True