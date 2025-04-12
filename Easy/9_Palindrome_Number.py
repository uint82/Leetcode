
class Solution:
    def __init__(self, x: int) -> None:
        self.x = x

    def isPalindrome(self) -> bool:
        # Create a local variable        
        x = self.x
        
        # Numbers less than 0 are not palindromes because of the negative sign
        if x < 0:
            return False

        # Edge case: If x ends with 0, it's only a palindrome if it's 0
        if x % 10 == 0 and x != 0:
            return False
        
        # Reverse half of the number to check if it's a palindrome
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10
    
        # For even number of digits: x == reversed_half
        # For odd number of digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


# Test
test1 = Solution(121)
print(f"Test 1: Is 121 a palindrome? {test1.isPalindrome()}")  # Should return True

test2 = Solution(-121)
print(f"Test 2: Is -121 a palindrome? {test2.isPalindrome()}")  # Should return False

test3 = Solution(10)
print(f"Test 3: Is 10 a palindrome? {test3.isPalindrome()}")  # Should return False

test4 = Solution(0)
print(f"Test 4: Is 0 a palindrome? {test4.isPalindrome()}")  # Should return True

test5 = Solution(12321)
print(f"Test 5: Is 12321 a palindrome? {test5.isPalindrome()}")  # Should return True

test6 = Solution(1221)
print(f"Test 6: Is 1221 a palindrome? {test6.isPalindrome()}")  # Should return True

test7 = Solution(1234)
print(f"Test 7: Is 1234 a palindrome? {test7.isPalindrome()}")  # Should return False

test8 = Solution(1000021)
print(f"Test 8: Is 1000021 a palindrome? {test8.isPalindrome()}")  # Should return False

# Edge cases
test9 = Solution(11)
print(f"Test 9: Is 11 a palindrome? {test9.isPalindrome()}")  # Should return True

test10 = Solution(1)
print(f"Test 10: Is 1 a palindrome? {test10.isPalindrome()}")  # Should return True
