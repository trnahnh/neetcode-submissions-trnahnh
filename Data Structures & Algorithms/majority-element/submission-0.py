class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = count = 0

        for num in nums:
            freq[num] += 1
            if count < freq[num]:
                res = num
                count = freq[num]
        return res