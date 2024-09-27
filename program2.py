class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass


def romanToInt(s: str) -> int:
    # Define a dictionary to map Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through the string in reverse order
    for char in reversed(s):
        current_value = roman_values[char]
        
        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            # Otherwise, add it to the total
            total += current_value
        
        # Update the previous value to the current value
        prev_value = current_value
    
    return total

# Test cases
print(romanToInt("III"))    # Output: 3
print(romanToInt("IV"))     # Output: 4
print(romanToInt("IX"))     # Output: 9
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV"))# Output: 1994

