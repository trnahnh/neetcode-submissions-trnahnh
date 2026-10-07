class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pd = set()
        nd = set()

        res = 0
        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in pd or (r - c) in nd:
                    continue
                
                col.add(c)
                pd.add(r + c)
                nd.add(r - c)

                dfs(r + 1)

                col.remove(c)
                pd.remove(r + c)
                nd.remove(r - c)
            
        dfs(0)
        return res