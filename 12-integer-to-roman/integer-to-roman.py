class Solution:
    def intToRoman(self, num):
        # Define the Roman numeral symbols and their corresponding values
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        # Initialize the result string
        result = []
        
        # Iterate through the values and symbols
        for i in range(len(values)):
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]
        
        # Join the result list into a single string and return it
        return "".join(result)