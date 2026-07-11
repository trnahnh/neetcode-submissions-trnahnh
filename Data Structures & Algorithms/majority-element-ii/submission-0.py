class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        res = []

        for count in counts:
            if counts[count] > len(nums) / 3:
                res.append(count)
        
        return res