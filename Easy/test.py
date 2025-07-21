

class Solution:
    def __init__(self, num: int) -> None:
        self.num = num

    def is_palindrome(self) -> bool:
        if self.num < 0:
            return False

        if self.num % 10 == 0 and self.num != 0:
            return False

        mirror = 0

        # 12521

        while mirror < self.num:
            mirror = (self.num % 10) + (mirror * 10)
            self.num = self.num // 10
        return self.num == mirror or mirror // 10 == self.num

# test
test: Solution = Solution(12521)
print(test.is_palindrome())
