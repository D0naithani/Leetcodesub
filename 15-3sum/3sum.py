class Solution:
    def threeSum(self, nums):
        # Sort the array to enable the two-pointer approach
        nums.sort()
        result = []
        n = len(nums)  # Store the length of the array
        
        for i in range(n - 2):
            # Early termination: If the current number is greater than zero, no triplet can sum to zero
            if nums[i] > 0:
                break
            
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find the other two elements
            left, right = i + 1, n - 1
            target = -nums[i]  # The target sum for the two-pointer search
            
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer to the next distinct value
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the next distinct value
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward
                    left += 1
                    right -= 1
                
                elif total < target:
                    # Increase the sum by moving the left pointer
                    left += 1
                else:
                    # Decrease the sum by moving the right pointer
                    right -= 1
        
        return result