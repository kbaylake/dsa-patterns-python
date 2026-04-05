# 49. Group Anagram
# 05-04-2026
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana={}
        for s in strs:
            l1=[i for i in s]
            l1.sort()
            gram=''.join(l1)
            if gram in ana:
                ana[gram].append(s)
            else:
                ana[gram]=[s]
        return list(ana.values())