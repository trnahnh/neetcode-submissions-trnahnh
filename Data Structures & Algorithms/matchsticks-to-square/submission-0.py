class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        length = total // 4
        if max(matchsticks) > length:
            return False
        
        n = len(matchsticks)
        memo = {}

        def dfs(mask):
            if mask == 0:
                return 0
            if mask in memo:
                return memo[mask]
            
            for i in range(n):
                if mask & (1 << i):
                    prev_len = dfs(mask ^ (1 << i))
                    
                    if prev_len >= 0 and prev_len + matchsticks[i] <= length:
                        memo[mask] = (prev_len + matchsticks[i]) % length
                        return memo[mask]
            
            memo[mask] = -1
            return -1

        return dfs((1 << n) - 1) == 0