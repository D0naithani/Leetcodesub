class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage:
solution = Solution()
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height1))  # Output: 49

height2 = [1, 1]
print(solution.maxArea(height2))  # Output: 1