class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        # write code here
        # write code here
        head = pHead
        mp = dict()
        # mp[head.val] = 1
        while head:
            if not mp.get(head.val):
                mp[head.val] = 1
            else:
                mp[head.val] = mp[head.val] + 1
            head = head.next
        head1 = ListNode(0)
        head1.next = pHead
        head = head1
        while head.next:
            if mp.get(head.next.val) > 1:
                head.next = head.next.next
                continue
            head = head.next
        return head1.next
