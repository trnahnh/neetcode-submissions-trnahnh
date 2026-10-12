class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indeg = [0] * numCourses
        for nxt, pre in prerequisites:
            indeg[nxt] += 1
            adj[pre].append(nxt)
        
        res = []

        def dfs(node):
            res.append(node)
            indeg[node] -= 1
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    dfs(nei)
        
        for i in range(numCourses):
            if indeg[i] == 0:
                dfs(i)
        
        return res if len(res) == numCourses else []