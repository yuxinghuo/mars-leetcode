class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        res = None
        i = 0
        while head:
            node = ListNode(head.val)
            if i == 0:
                res = node
            else:
                node.next = res
                res = node
            head = head.next
            i += 1
        return res


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        head = pHead
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre 
