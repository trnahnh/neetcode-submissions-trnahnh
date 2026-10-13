class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [float('inf')] * (rows * cols)
        dist[0] = 0
        inq = [False] * (rows * cols)

        def index(r, c):
            return r * cols + c
        
        queue = deque([0])
        inq[0] = True
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            u = queue.popleft()
            inq[u] = False
            r, c = divmod(u, cols)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nr < cols:
                    v = index(nr, nc)
                    weight = abs(heights[r][c] - heights[nr][nc])
                    nd = max(dist[u], weight)
                    if nd < dist[v]:
                        dist[v] = nd
                        if not inq[v]:
                            queue.append(v)
                            inq[v] = True
        
        return dist[rows * cols - 1]