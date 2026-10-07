class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, 0)
        return self.res
    
    def dfs(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.dfs(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]