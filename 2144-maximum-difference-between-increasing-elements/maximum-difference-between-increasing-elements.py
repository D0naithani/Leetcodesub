from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = float('inf')
        max_diff = -1

        for j in range(len(nums)):
            if nums[j] > min_so_far:
                diff = nums[j] - min_so_far
                max_diff = max(max_diff, diff)
            else:
                min_so_far = min(min_so_far, nums[j])

        return max_diff if max_diff != 0 else -1