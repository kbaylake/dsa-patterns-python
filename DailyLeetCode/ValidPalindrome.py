# 125. Valid Palindrome
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ls=[c for c in s if c.isalnum()]
        return ls[::-1]==ls