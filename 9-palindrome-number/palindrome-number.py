class Solution:
    def isPalindrome(self, x):
        # Edge case: Negative numbers and numbers ending with 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Reverse half of the digits
        while x > reversed_half:
            last_digit = x % 10
            reversed_half = reversed_half * 10 + last_digit
            x //= 10
        
        # Check if the number is a palindrome
        return x == reversed_half or x == reversed_half // 10