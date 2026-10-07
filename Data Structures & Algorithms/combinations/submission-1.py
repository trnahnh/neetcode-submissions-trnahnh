class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, curList):
            if len(curList) == k:
                res.append(curList.copy())
                return
            
            if i > n:
                return

            curList.append(i)
            dfs(i + 1, curList)
            curList.pop()
            dfs(i + 1, curList)

        dfs(1, [])
        return res
        