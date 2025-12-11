class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        #一个已经为空了，直接返回另一个
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        #加一个表头
        head = ListNode(0)
        cur = head
        #两个链表都要不为空
        while pHead1 and pHead2:
            #取较小值的节点
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                #只移动取值的指针
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                #只移动取值的指针
                pHead2 = pHead2.next
            #指针后移
            cur = cur.next
        #哪个链表还有剩，直接连在后面
        if pHead1:
            cur.next = pHead1
        else:
            cur.next = pHead2
        #返回值去掉表头
        return head.next
