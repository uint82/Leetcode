

class Solution:

    def __init__(self, x: int) -> None:
        self.x = x

    def is_palindrome(self) -> bool:

        x = self.x

        if x < 0:
            return False

        if x % 10 == 0 and x != 0:
            return False

        half = 0

        while half < x:
            half = (x % 10) + (half * 10)
            x = x // 10
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
