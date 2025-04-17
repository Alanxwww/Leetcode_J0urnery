''''
Reverse Linked List 
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
    Input: head = [0,1,2,3]
    Output: [3,2,1,0]
'''
from typing import Optional

class ListNode:
    """Defines a node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        """Creates a linked list from a Python list."""
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def print_list(head):
        """Prints the linked list."""
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def __str__(self):
        """String representation of the linked list."""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result) + " -> None"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursively reverses a singly linked list."""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        print("newHead", newHead, "||head||",head, "||next:", head.next)

        head.next.next = head
        head.next = None

        return newHead
        

# Example usage
head = ListNode.from_list([0, 1, 2, 3, 4])
print("Original: ", end="")
ListNode.print_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed:")
ListNode.print_list(reversed_head)