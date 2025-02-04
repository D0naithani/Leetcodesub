class Solution:
    def maxArea(self, height):
        # Initialize two pointers
        left, right = 0, len(height) - 1
        max_area = 0
        
        # Use two-pointer approach to find the maximum area
        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer corresponding to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area