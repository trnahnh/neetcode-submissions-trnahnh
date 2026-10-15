class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        pre = suf = 0

        for i in range(n):
            pre = nums[i] * (pre or 1)
            suf = nums[n - 1 - i] * (suf or 1)
            res = max(res, max(pre, suf))
        return res