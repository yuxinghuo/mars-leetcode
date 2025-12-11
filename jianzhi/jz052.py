import re
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        l1,l2=pHead1,pHead2
        while l1 != l2:
            l1=pHead2 if l1 is None else l1.next
            l2=pHead1 if l2 is None else l2.next
        return l1