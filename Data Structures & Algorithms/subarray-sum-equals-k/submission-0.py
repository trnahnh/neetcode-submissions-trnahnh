class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        for i in nums:
            if nums[i] == k:
                count += 1
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == k:
                    count += 1
                else:
                    break
                j += 1
            i += 1

        return count