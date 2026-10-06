class Solution:

    def dfs( self,i, nums : List[int], subset : List[[List[int]]], curset : List[int]):

        if i >= len(nums):
            subset.append(curset.copy())
            return
        curset.append(nums[i])
        self.dfs(i+1,nums,subset,curset)

        curset.pop()
        self.dfs(i+1,nums,subset,curset)
        


    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        curset = []

        self.dfs(0,nums,subset,curset)
        return subset