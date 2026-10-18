class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [0] * n
        rightMax[-1] = nums[-1]
        suffixSum = nums[-1]

        for i in range(n - 2, -1, -1):
            suffixSum += nums[i]
            rightMax[i] = max(rightMax[i + 1], suffixSum)
        
        maxSum = nums[0]
        currMax = 0
        prefixSum = 0

        for i in range(n):
            currMax = max(currMax, 0) + nums[i]
            maxSum = max(maxSum, currMax)
            prefixSum += nums[i]
            if i + 1 < n:
                maxSum = max(maxSum, prefixSum + rightMax[i + 1])
        
        return maxSum