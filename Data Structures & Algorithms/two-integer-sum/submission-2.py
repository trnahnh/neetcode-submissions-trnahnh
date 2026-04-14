class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) + 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
            j += 1
        i += 1
        
        return -1