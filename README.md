# LeetCode Solutions

This repository contains my solutions to various LeetCode problems implemented in Python. Each solution includes detailed comments explaining the approach, algorithm, and time/space complexity analysis.

## Repository Structure

Solutions are organized by difficulty level in separate folders:

```
/easy
    - 001_two_sum.py
    - 020_valid_parentheses.py
    - ...

/medium
    - 011_container_with_most_water.py
    - 015_3sum.py
    - ...

/hard
    - 004_median_of_two_sorted_arrays.py
    - 023_merge_k_sorted_lists.py
    - ...

/daily
    - 1431_minimum_difficulty_of_a_job_schedule.py
    - 4342_pascals_triangle_ii.py
    - ...
```

Within each difficulty folder, solutions follow the naming convention: `problem_number_problem_name.py` (or date-based naming for daily challenges).

## Solution Format

Each solution file typically includes:

- Problem statement and constraints as comments
- My approach explanation
- Time and space complexity analysis
- Edge cases consideration
- The solution code with inline comments

Example format:
```python
"""
Problem #1: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Approach:
- Use a hash map to store visited numbers and their indices
- For each number, check if (target - current number) exists in our map
- If found, return both indices
- Otherwise, add current number and its index to the map

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - storing up to n elements in the hash map
"""

def twoSum(nums, target):
    # Hash map to store visited numbers and their indices
    seen = {}
    
    for i, num in enumerate(nums):
        # Check if complement exists in our map
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
            
        # Store current number and its index
        seen[num] = i
    
    # No solution found
    return []
```

## Topics Covered

Solutions in this repository cover various data structures and algorithms including:

- Arrays and Strings
- Linked Lists
- Hash Tables
- Sliding Window

## Progress Tracking

| Category | Number of Problems Solved |
|----------|---------------------------|
| Easy     | 6                         |
| Medium   | 0                         |
| Hard     | 0                         |
| Total    | 6                         |

## Goals

My objectives for this LeetCode journey:
- Improve problem-solving skills
- Master common algorithms and data structures
- Prepare for technical interviews
- Document my learning process

## Connect With Me

I'm always open to discussing algorithmic approaches or receiving feedback on my solutions!

- **GitHub**: [[uint82](https://github.com/uint82)]
- **LinkedIn**: [[Hilmi Abroor](https://www.linkedin.com/in/hilmi-abror-022123204/)]
- **LeetCode Profile**: [[uint82](https://leetcode.com/u/uint82/)]
- **Email**: [abrorhilmi6@gmail.com]

Feel free to open an issue or submit a pull request if you have suggestions for improving any solution.

## Study Resources

Resources I've found helpful in my LeetCode journey:

- **Books**:
  - "Cracking the Coding Interview" by Gayle Laakmann McDowell
  - "Elements of Programming Interviews" by Adnan Aziz, Tsung-Hsien Lee, and Amit Prakash
  - "Algorithms" by Robert Sedgewick and Kevin Wayne

- **Websites**:
  - [LeetCode](https://leetcode.com/)
  - [NeetCode](https://neetcode.io/)
  - [Algorithms Visualized](https://visualgo.net/)
  - [Blind 75 Question List](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)

## My Problem-Solving Approach

When tackling a new problem, I typically follow these steps:
1. Understand the problem thoroughly
2. Think of a brute force solution first
3. Optimize by identifying patterns or applying specific algorithms
4. Test with examples and edge cases
5. Code the solution with clear comments
6. Analyze time and space complexity

## Patterns & Techniques Mastered

- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Binary Search
- [ ] Breadth-First Search
- [ ] Depth-First Search
- [ ] Dynamic Programming


## License

This repository is available under the [MIT License](LICENSE).
