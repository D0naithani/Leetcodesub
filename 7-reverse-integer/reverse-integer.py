class Solution:
    def reverse(self, x):
        # Define the 32-bit integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Handle the sign of the input
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        
        while x > 0:
            # Extract the last digit
            last_digit = x % 10
            x //= 10
            
            # Check for overflow before updating reversed_num
            if reversed_num > (INT_MAX - last_digit) // 10:
                return 0  # Overflow detected
            
            # Append the last digit to reversed_num
            reversed_num = reversed_num * 10 + last_digit
        
        # Restore the sign and return the result
        return sign * reversed_num