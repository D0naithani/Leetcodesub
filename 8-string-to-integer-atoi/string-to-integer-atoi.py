class Solution:
    def myAtoi(self, s):
        # Define the 32-bit signed integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Initialize variables
        n = len(s)
        i = 0
        result = 0
        sign = 1  # Default to positive
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Determine the sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Parse digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            
            # Append the current digit to the result
            result = result * 10 + digit
            i += 1
        
        # Step 4: Apply the sign and return the result
        return sign * result