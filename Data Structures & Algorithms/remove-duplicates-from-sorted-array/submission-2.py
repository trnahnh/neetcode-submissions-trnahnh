class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 1
        j = 1

        if (n == 0 or n == 1):
            return n
        
        while j < n:
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        return i