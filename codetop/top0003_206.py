# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return_node = None
        curr = head
        while curr:
            next = curr.next
            curr.next = return_node
            return_node = curr
            curr = next
        return return_node

    def test2(self, head: ListNode) -> ListNode:
        return_node = None
        curr = head
        while curr:
            next = curr.next
            curr.next = return_node
            return_node = curr
            curr = next
        return return_node
