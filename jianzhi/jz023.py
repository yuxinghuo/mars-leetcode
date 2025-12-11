# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead: ListNode):
        # write code here
        dict1 = {}
        while pHead:
            if dict1.get(pHead.val):
                return pHead
            else:
                dict1[pHead.val] = 1
                pHead = pHead.next

        return None
