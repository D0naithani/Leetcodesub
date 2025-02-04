class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate height and width directly
            h_left, h_right = height[left], height[right]
            area = (h_left if h_left < h_right else h_right) * (right - left)
            
            # Update max_area if the current area is larger
            if area > max_area:
                max_area = area
            
            # Move the pointer corresponding to the shorter line
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        
        return max_area