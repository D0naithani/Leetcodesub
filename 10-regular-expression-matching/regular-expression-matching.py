class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # Use two rows instead of a full DP table to save space
        prev = [False] * (n + 1)
        curr = [False] * (n + 1)
        
        # Base case: Empty string matches empty pattern
        prev[0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* that match an empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]
        
        # Fill the DP table row by row
        for i in range(1, m + 1):
            curr[0] = False  # Reset the first column for the current row
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    # Direct match or '.' match
                    curr[j] = prev[j - 1]
                elif p[j - 1] == '*':
                    # Case 1: '*' acts as zero occurrences of the preceding character
                    curr[j] = curr[j - 2]
                    # Case 2: '*' acts as one or more occurrences of the preceding character
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        curr[j] = curr[j] or prev[j]
                else:
                    curr[j] = False  # No match
            
            # Swap prev and curr for the next iteration
            prev, curr = curr, [False] * (n + 1)
        
        return prev[n]