class Solution:
    def queryResults(self, limit, queries):
        # Dictionary to track the current color of each ball
        color_map = {}
        # Dictionary to track the frequency of each color
        color_count = {}
        # List to store the result after each query
        result = []
        
        for x, y in queries:
            # Use local variables to avoid repeated dictionary lookups
            old_color = color_map.get(x, None)
            
            # If the ball already has a color, decrement its count
            if old_color is not None:
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            
            # Assign the new color to the ball
            color_map[x] = y
            # Increment the count of the new color
            color_count[y] = color_count.get(y, 0) + 1
            
            # Append the number of distinct colors to the result
            result.append(len(color_count))
        
        return result