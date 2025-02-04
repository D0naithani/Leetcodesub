class Solution:
    def intToRoman(self, num):
        # Define Roman numeral symbols and their corresponding values
        mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        # Initialize the result as a list for faster appends
        result = []
        
        # Iterate through the mapping
        for value, symbol in mapping:
            while num >= value:
                result.append(symbol)
                num -= value
        
        # Join the result list into a single string and return it
        return "".join(result)