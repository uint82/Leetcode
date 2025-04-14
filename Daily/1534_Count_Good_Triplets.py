# !4 April 2025 Daily Leetcode problem
# this problem best solution is using nested loop 
# it might hurt your eyes 😆

class Solution:
    
    def __init__(self, arr: list[int], a: int, b: int, c: int) -> None:
        self.arr = arr
        self.a = a
        self.b = b
        self.c = c

    def countGoodTriplets(self) -> int:
        # Create a local variable
        arr = self.arr
        a = self.a
        b = self.b
        c = self.c

        n = len(arr)
        count = 0

        # loop to check the first condition then we check both condition
        # why? for optimization, then can we use condition 2 or 3 instead 1?
        # yes but its limited since condition 2 need both j and k to evaluate the condition
        # cause we haven't defined j and k
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if (abs(arr[j] - arr[k]) <= b and 
                            abs(arr[i] - arr[k]) <= c):
                            count += 1
        return count

# Test cases
test1 = Solution([3, 0, 1, 1, 9, 7], 7, 2, 3)
result1 = test1.countGoodTriplets()
print(f"Test 1: {result1}")  # Should return 4

test2 = Solution([1, 1, 2, 2, 3], 0, 0, 1)
result2 = test2.countGoodTriplets()
print(f"Test 2: {result2}")  # Should return 0

# Additional test cases
test3 = Solution([7, 3, 7, 3, 12, 1, 12, 2, 3], 5, 8, 1)
result3 = test3.countGoodTriplets()
print(f"Test 3: {result3}") # should return 12

test4 = Solution([1, 2, 3], 1, 1, 1)
result4 = test4.countGoodTriplets()
print(f"Test 4: {result4}") # should return 0

# Edge case test
print("\nEdge case tests:")
edge_test1 = Solution([5, 5, 5], 0, 0, 0)
edge_result1 = edge_test1.countGoodTriplets()
print(f"Edge Test 1 (identical elements): {edge_result1}")

edge_test2 = Solution([1000, 1000, 1000], 1000, 1000, 1000)
edge_result2 = edge_test2.countGoodTriplets()
print(f"Edge Test 2 (max constraints): {edge_result2}")









