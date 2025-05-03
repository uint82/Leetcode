
class Solution:

    def __init__(self, s: str) -> None:
        self.s = s

    def is_valid(self) -> bool:
        
        pairs = { ')': '(', '}': '{', ']': '[' }
        stack = []
        
        for char in self.s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

# test
test = Solution("[(){()}]")
print(test.is_valid())


