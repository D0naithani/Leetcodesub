class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:  # Edge case: empty input array
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the array
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                if not prefix:  # If the prefix becomes empty, return ""
                    return ""
        
        return prefix