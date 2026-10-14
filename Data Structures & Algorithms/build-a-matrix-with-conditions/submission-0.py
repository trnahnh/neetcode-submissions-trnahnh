class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True
        
        def sorting(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)
            
            visit, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if src not in visit:
                    if not dfs(src, adj, visit, path, order):
                        return []
            return order[::-1]
        
        row_order = sorting(rowConditions)
        if not row_order:
            return []
        
        col_order = sorting(colConditions)
        if not col_order:
            return []
        
        valR = {num: i for i, num in enumerate(row_order)}
        valC = {num: i for i, num in enumerate(col_order)}
        res = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r, c = valR[num], valC[num]
            res[r][c] = num
        
        return res