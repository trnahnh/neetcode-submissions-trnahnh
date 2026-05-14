class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times number appears
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # Empty list for each possible frequency
        frequency = []
        for _ in range(len(nums) + 1):
            frequency.append([])
        
        # Place number to match frequency
        for n, c in count.items():
            frequency[c].append(n)
        
        # Traverse value top down to have highest k
        result = []
        for i in range(len(frequency) -1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result