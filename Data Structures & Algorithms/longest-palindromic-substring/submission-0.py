class Solution:
    def longestPalindrome(self, s: str) -> str:
        resI = 0
        resL = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resL:
                    resI = 1
                    resL = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resL:
                    resI = l
                    resL = r - l + 1
                l -= 1
                r += 1
            
        return s[resI : resI + resL]