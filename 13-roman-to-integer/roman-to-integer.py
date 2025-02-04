class Solution:
    def romanToInt(self, s):
        # Create a dictionary to map Roman numeral symbols to their values
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # Initialize the result
        total = 0
        
        # Traverse the string
        for i in range(len(s)):
            # Get the value of the current numeral
            current_value = roman_to_int[s[i]]
            
            # If the current numeral is smaller than the next numeral, subtract it
            if i + 1 < len(s) and current_value < roman_to_int[s[i + 1]]:
                total -= current_value
            else:
                # Otherwise, add it
                total += current_value
        
        return total