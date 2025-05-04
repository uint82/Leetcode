"""
Problem #9: Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Examples:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it reads 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Approach:
- Handle edge cases first:
  - Negative numbers are not palindromes (due to the minus sign).
  - Numbers ending with 0 are not palindromes (except 0 itself).
- Reverse half of the number and compare with the other half.
- For numbers with odd digits, the middle digit is ignored in the comparison.
- This approach avoids converting to string and uses O(1) space.

Time Complexity: O(log n) — where n is the input number (number of digits)
Space Complexity: O(1) — only using a constant amount of space
"""

class Solution:

    def __init__(self, x: int) -> None:
        self.x = x

    def is_palindrome(self) -> bool:

        x = self.x

        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending with 0 are not palindromes (except 0 itself)
        if x % 10 == 0 and x != 0:
            return False

        half = 0

        # Reverse the second half of the number
        while half < x:
            half = (x % 10) + (half * 10)
            x = x // 10
            
        # For even number of digits: half == x
        # For odd number of digits: half // 10 == x (to ignore the middle digit)
        return half == x or half // 10 == x

# Test
test1 = Solution(121)
print(f"Test 1: Is 121 a palindrome? {test1.is_palindrome()}")  # Should return True

test2 = Solution(-121)
print(f"Test 2: Is -121 a palindrome? {test2.is_palindrome()}")  # Should return False

test3 = Solution(10)
print(f"Test 3: Is 10 a palindrome? {test3.is_palindrome()}")  # Should return False

test4 = Solution(0)
print(f"Test 4: Is 0 a palindrome? {test4.is_palindrome()}")  # Should return True

test5 = Solution(12321)
print(f"Test 5: Is 12321 a palindrome? {test5.is_palindrome()}")  # Should return True

test6 = Solution(1221)
print(f"Test 6: Is 1221 a palindrome? {test6.is_palindrome()}")  # Should return True

test7 = Solution(1234)
print(f"Test 7: Is 1234 a palindrome? {test7.is_palindrome()}")  # Should return False

test8 = Solution(1000021)
print(f"Test 8: Is 1000021 a palindrome? {test8.is_palindrome()}")  # Should return False

# Edge cases
test9 = Solution(11)
print(f"Test 9: Is 11 a palindrome? {test9.is_palindrome()}")  # Should return True

test10 = Solution(1)
print(f"Test 10: Is 1 a palindrome? {test10.is_palindrome()}")  # Should return True
