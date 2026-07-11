class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0

        for num in n:
            if (num - 1) not in n:
                length = 1
                while (num + length) in n:
                    length += 1
                longest = max(length, longest)
        return longest