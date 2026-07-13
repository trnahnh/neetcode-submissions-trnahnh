class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = [nums[0]]
        i = 0
        j = 1

        while j < len(nums):
            if nums[j] != nums[i]:
                res.append(nums[j])
                i = j
            j += 1

        k = len(res)
        for idx in range(k):
            nums[idx] = res[idx]

        return k