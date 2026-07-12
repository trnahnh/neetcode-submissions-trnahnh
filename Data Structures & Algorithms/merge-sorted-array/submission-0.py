class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        res = []

        # array same length
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        # nums 2 still have values
        while j < n:
            res.append(nums2[j])
            j += 1
        
        # nums 1 still have values
        while i < m:
            res.append(nums1[i])
            i += 1
            
        for idx in range(m + n):
            nums1[idx] = res[idx]