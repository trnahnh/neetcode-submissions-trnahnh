class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        missing = 1
        while missing in nums_set:
            missing += 1
        return missing