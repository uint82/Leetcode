"""
Problem #20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true

Approach:
- Use a stack to keep track of opening brackets.
- Create a hash map that maps closing brackets to their corresponding opening brackets.
- Iterate through the string:
  - If the current character is a closing bracket:
    - Check if the stack is empty or the top of the stack doesn't match the corresponding opening bracket.
    - If either condition is true, return false.
    - Otherwise, pop the top element from the stack.
  - If the current character is an opening bracket, push it onto the stack.
- After processing all characters, the stack should be empty for a valid string.

Time Complexity: O(n) — where n is the length of the string
Space Complexity: O(n) — in the worst case, the stack could contain all opening brackets
"""

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

# Basic test cases
test1 = Solution("()")
print(f"Test 1: '()' should be True: {test1.is_valid()}")  # Should return True

test2 = Solution("()[]{}")
print(f"Test 2: '()[]{{}}' should be True: {test2.is_valid()}")  # Should return True

test3 = Solution("(]")
print(f"Test 3: '(]' should be False: {test3.is_valid()}")  # Should return False

test4 = Solution("([)]")
print(f"Test 4: '([)]' should be False: {test4.is_valid()}")  # Should return False

test5 = Solution("{[]}")
print(f"Test 5: '{{[]}}' should be True: {test5.is_valid()}")  # Should return True

# Nested brackets
test6 = Solution("[(){()}]")
print(f"Test 6: '[(){{()}}]' should be True: {test6.is_valid()}")  # Should return True

test7 = Solution("(({{[[]]}}))") 
print(f"Test 7: '(({{[[]]}}))' should be True: {test7.is_valid()}")  # Should return True

test8 = Solution("({[()]})") 
print(f"Test 8: '({{[()]}}))' should be True: {test8.is_valid()}")  # Should return True

# Edge cases
test9 = Solution("")
print(f"Test 9: '' (empty string) should be True: {test9.is_valid()}")  # Should return True (empty string is valid)

test10 = Solution("(")
print(f"Test 10: '(' should be False: {test10.is_valid()}")  # Should return False (unclosed bracket)

test11 = Solution(")")
print(f"Test 11: ')' should be False: {test11.is_valid()}")  # Should return False (no opening bracket)

# Unbalanced brackets
test12 = Solution("((")
print(f"Test 12: '((' should be False: {test12.is_valid()}")  # Should return False (unclosed brackets)

test13 = Solution("))")
print(f"Test 13: '))' should be False: {test13.is_valid()}")  # Should return False (no opening brackets)

test14 = Solution("()[]{")
print(f"Test 14: '()[]{{' should be False: {test14.is_valid()}")  # Should return False (unclosed bracket)

test15 = Solution("([]")
print(f"Test 15: '([]' should be False: {test15.is_valid()}")  # Should return False (unclosed bracket)

# Incorrect order
test16 = Solution("([)]")
print(f"Test 16: '([)]' should be False: {test16.is_valid()}")  # Should return False (incorrect order)

test17 = Solution("{(})")
print(f"Test 17: '{{(}})' should be False: {test17.is_valid()}")  # Should return False (incorrect order)

# Complex cases
test18 = Solution("{[()]}()(()[]){{}}[]")
print(f"Test 18: '{{[()]}}()(()[]){{}}[]' should be True: {test18.is_valid()}")  # Should return True

test19 = Solution("((()(())))") 
print(f"Test 19: '((()(())))' should be True: {test19.is_valid()}")  # Should return True

test20 = Solution("({[]}){[]{()}}") 
print(f"Test 20: '({{[]}}){{[]{{()}}}}' should be True: {test20.is_valid()}")  # Should return True
