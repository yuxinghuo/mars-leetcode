class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param val int整型
# @return ListNode类
#
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # write code here
        if head.val == val:
            return head.next
        start = head
        while start.next is not None:
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next
        return head
