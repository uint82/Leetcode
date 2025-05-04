"""
Problem #13: Roman to Integer

Convert a Roman numeral to an integer.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol values:
- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

Roman numerals are usually written largest to smallest from left to right, but there are special cases:
- IV = 4 (5-1)
- IX = 9 (10-1)
- XL = 40 (50-10)
- XC = 90 (100-10)
- CD = 400 (500-100)
- CM = 900 (1000-100)

Example:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.

Approach:
- Create a hash map to store the values of Roman symbols.
- Iterate through the string from left to right.
- Compare the current symbol with the next one:
  - If the current symbol has a smaller value than the next one, subtract it (special case).
  - Otherwise, add its value to the result.
- Use a skip flag to handle cases where two symbols form a special case.

Time Complexity: O(n) — where n is the length of the input string
Space Complexity: O(1) — constant space for the symbol value dictionary
"""

class Solution:

    def __init__(self, s: str) -> None:
        self.s = s

    def romanToInt(self) -> int:
        # create a local variable
        s = self.s

        # every roman symbol value inside a dictionary
        symbol_value: dict[str, int] = {
                "I": 1,
                "V": 5,
                "X": 10, 
                "L": 50, 
                "C": 100, 
                "D": 500, 
                "M": 1000,
        }

        n = len(s)

        result = 0
        skip = False
        
        # i compare the first 
        for i in range(n):
            current = s[i]
            
            if skip:
                skip = False
                continue

            if i + 1 < n:
                next = s[i + 1]
                
                if symbol_value[current] < symbol_value[next]:
                    result += symbol_value[next] - symbol_value[current]
                    skip = True
                else:
                    result += symbol_value[current]

            else:
                result += symbol_value[current]

        return result

# test
# Basic test cases
test1 = Solution("III")
print(f"Test 1: 'III' should be 3: {test1.romanToInt()}")  # Should return 3

test2 = Solution("IV")
print(f"Test 2: 'IV' should be 4: {test2.romanToInt()}")  # Should return 4

test3 = Solution("IX")
print(f"Test 3: 'IX' should be 9: {test3.romanToInt()}")  # Should return 9

test4 = Solution("LVIII")
print(f"Test 4: 'LVIII' should be 58: {test4.romanToInt()}")  # Should return 58 (L=50, V=5, III=3)

test5 = Solution("MCMXCIV")
print(f"Test 5: 'MCMXCIV' should be 1994: {test5.romanToInt()}")  # Should return 1994 (M=1000, CM=900, XC=90, IV=4)

# Edge cases
test6 = Solution("I")
print(f"Test 6: 'I' should be 1: {test6.romanToInt()}")  # Should return 1

test7 = Solution("MMMCMXCIX")
print(f"Test 7: 'MMMCMXCIX' should be 3999: {test7.romanToInt()}")  # Should return 3999 (largest valid Roman numeral)

# All possible subtraction cases
test8 = Solution("IV")  # 4
test9 = Solution("IX")  # 9
test10 = Solution("XL")  # 40
test11 = Solution("XC")  # 90
test12 = Solution("CD")  # 400
test13 = Solution("CM")  # 900
print(f"Test 8-13: Subtraction cases:")
print(f"  'IV' should be 4: {test8.romanToInt()}")
print(f"  'IX' should be 9: {test9.romanToInt()}")
print(f"  'XL' should be 40: {test10.romanToInt()}")
print(f"  'XC' should be 90: {test11.romanToInt()}")
print(f"  'CD' should be 400: {test12.romanToInt()}")
print(f"  'CM' should be 900: {test13.romanToInt()}")

# Complex cases
test14 = Solution("MDCLXVI")
print(f"Test 14: 'MDCLXVI' should be 1666: {test14.romanToInt()}")  # Should return 1666 (all symbols in descending order)

test15 = Solution("MCDXLIV")
print(f"Test 15: 'MCDXLIV' should be 1444: {test15.romanToInt()}")  # Should return 1444 (M=1000, CD=400, XL=40, IV=4)
