class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        mapping = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            mapping[b].append(a)
        
        cache = {}

        def dfs(course):
            if course not in cache:
                cache[course] = set()

                for n in mapping[course]:
                    cache[course].update(dfs(n))
                    cache[course].add(n)
                
            return cache[course]
        
        for i in range(numCourses):
            dfs(i)
        
        solution = []
        for a,b in queries:
            if a in cache[b]:
                solution.append(True)
            else:
                solution.append(False)
        return solution