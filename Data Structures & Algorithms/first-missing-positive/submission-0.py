class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        mins = nums[0]
        for i in nums:
            if nums[i] > mins:
                mins = nums[i]
            i += 1
        mins += 1
        
        return mins