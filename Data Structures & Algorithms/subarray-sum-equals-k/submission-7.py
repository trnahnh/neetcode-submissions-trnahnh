class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for num in nums:
            total += num
            count += prefix_sum[total - k]
            prefix_sum[total] += 1

        return count