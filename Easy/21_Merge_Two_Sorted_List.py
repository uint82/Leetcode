"""
Problem #21: Merge Two Sorted Lists

Given the heads of two sorted linked lists `list1` and `list2`, merge the two lists into one sorted list.
Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Approach:
- Create a dummy head node to simplify edge cases.
- Use a pointer to track the current position in the result list.
- Compare values from both lists and take the smaller one.
- Append the chosen node to the result list and advance its pointer.
- When one list is exhausted, append the remainder of the other list.
- Return the next node after the dummy head (the actual head of the merged list).

Time Complexity: O(n + m) — where n and m are the lengths of the two lists
Space Complexity: O(1) — only using pointers, no additional data structures
"""

class ListNode(object):

    def __init__(self, val: int =  0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    
    def Merge(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        head = ListNode(0)
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return head.next

    def nodetoArray(self, head: ListNode | None) -> list[int]:

        current = head
        result = []

        while current:
            result.append(current.val)
            current = current.next
        return result

# test
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

test = Solution()
merged = test.Merge(l1, l2)
result = test.nodetoArray(merged)
print(result)
