class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the height and width
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            
            # Update max_area
            if area > max_area:
                max_area = area
            
            # Move the pointer corresponding to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area