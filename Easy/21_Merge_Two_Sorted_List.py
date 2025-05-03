
class ListNode(object):

    def __init__(self, val: int =  0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    
    def Merge(self, list1: ListNode, list2: ListNode) -> ListNode:

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

    def nodetoArray(self, head: ListNode) -> list[int]:

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


