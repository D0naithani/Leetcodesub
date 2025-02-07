class Solution:
    def queryResults(self, limit, queries):
        ball_colors = {}  # To store the color of each ball
        color_counts = {}  # To count how many balls have each color
        distinct_colors = set()  # To store the distinct colors
        result = []  # To store the result after each query
        
        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                # Decrement the count for the old color
                color_counts[old_color] -= 1
                # If the count drops to 0, remove the color from distinct_colors
                if color_counts[old_color] == 0:
                    distinct_colors.discard(old_color)
            # Assign the new color to the ball
            ball_colors[x] = y
            # Increment the count for the new color
            if y in color_counts:
                color_counts[y] += 1
            else:
                color_counts[y] = 1
            # Add the new color to distinct_colors
            distinct_colors.add(y)
            # Append the number of distinct colors to the result
            result.append(len(distinct_colors))
        
        return result