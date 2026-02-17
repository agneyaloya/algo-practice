class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Optimal O(log(min(m, n))) solution using binary search
        on the smaller array to find the correct partition.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to minimize the search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        half = total_len // 2

        left, right = 0, m
        while True:
            i = (left + right) // 2  # partition in nums1
            j = half - i             # partition in nums2

            # Values just to the left and right of the partitions
            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < m else float("inf")

            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < n else float("inf")

            # Found correct partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total_len % 2:  # odd length
                    return float(min(nums1_right, nums2_right))
                return (max(nums1_left, nums2_left) +
                        min(nums1_right, nums2_right)) / 2.0

            # Need to move partition in nums1 to the left
            if nums1_left > nums2_right:
                right = i - 1
            # Need to move partition in nums1 to the right
            else:
                left = i + 1

