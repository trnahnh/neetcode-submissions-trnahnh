class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        ixx = 1
        inn = 1

        while inn <= n - 1:
            if ixx & x == 0:
                if inn & (n - 1):
                    res = res | ixx
                inn <<= 1
            ixx <<= 1
        
        return res