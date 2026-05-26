class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sol = []
        for i in range(2):
            for n in nums:
                sol.append(n)
        return sol