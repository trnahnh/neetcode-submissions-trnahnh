class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        seen = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for nei in adj[node]:
                if not seen[nei]:
                    seen[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not seen[node]:
                seen[node] = True
                dfs(node)
                res += 1
        return res