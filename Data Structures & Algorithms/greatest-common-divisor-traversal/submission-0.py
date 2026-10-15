class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if any(num == 1 for num in nums):
            return False
        
        m = max(nums)
        sieve = [0] * (m + 1)
        p = 2
        while p * p <= m:
            if sieve[p] == 0:
                for composite in range(p * p, m + 1, p):
                    sieve[composite] = p
            p += 1
        
        adj = defaultdict(list)
        for i in range(n):
            num = nums[i]
            if sieve[num] == 0:
                adj[i].append(n + num)
                adj[n + num].append(i)
                continue
            
            while num > 1:
                prime = sieve[num] if sieve[num] != 0 else num
                adj[i].append(n + prime)
                adj[n + prime].append(i)
                while num % prime == 0:
                    num //= prime
            
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        dfs(0)
        for i in range(n):
            if i not in visited:
                return False
        return True