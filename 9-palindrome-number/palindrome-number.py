class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x): return False
        r = 0
        while x > r: r, x = r * 10 + x % 10, x // 10
        return x in (r, r // 10)