class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                sub1 = s[left + 1 : right + 1]
                sub2 = s[left : right]
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]

            left += 1
            right -= 1
        
        return True