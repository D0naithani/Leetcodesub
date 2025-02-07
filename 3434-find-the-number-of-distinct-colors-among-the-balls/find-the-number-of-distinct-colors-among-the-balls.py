class Solution:
    def queryResults(self, limit, queries):
        # Dictionary to track the current color of each ball
        color_map = {}
        # Dictionary to track the frequency of each color
        color_count = {}
        # List to store the result after each query
        result = []
        
        append_result = result.append  # Local reference to reduce method lookup overhead
        
        for x, y in queries:
            old_color = color_map.get(x)  # Get the old color of ball x
            
            if old_color is not None:  # If the ball already has a color
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            
            # Assign the new color to the ball
            color_map[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            
            # Append the number of distinct colors to the result
            append_result(len(color_count))
        
        return result