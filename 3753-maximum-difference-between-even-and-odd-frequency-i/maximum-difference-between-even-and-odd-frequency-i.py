from collections import Counter

class Solution:
    def maxDifference(self, s):
        freq = Counter(s)

        odd_freqs = [v for v in freq.values() if v % 2 == 1]
        even_freqs = [v for v in freq.values() if v % 2 == 0]

        max_diff = float('-inf')
        for odd in odd_freqs:
            for even in even_freqs:
                max_diff = max(max_diff, odd - even)

        return max_diff
