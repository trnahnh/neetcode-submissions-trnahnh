class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        maxI = freq.index(max(freq))
        maxF = freq[maxI]
        if maxF > (len(s) + 1) // 2:
            return ""
        
        res = [''] * len(s)
        idx = 0
        maxC = chr(maxI + ord('a'))

        while freq[maxI] > 0:
            res[idx] = maxC
            idx += 2
            freq[maxI] -= 1
        
        for i in range(26):
            while freq[i] > 0:
                if idx >= len(s):
                    idx = 1
                res[idx] = chr(i + ord('a'))
                idx += 2
                freq[i] -= 1
        
        return ''.join(res)