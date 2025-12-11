class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        # write code here
        leftHead = pHead
        rightHead = pHead
        for i in range(0, k):
            if not rightHead:
                return None
            else:
                rightHead = rightHead.next
        while rightHead:
            rightHead = rightHead.next
            leftHead = leftHead.next
        return leftHead


solution = Solution()
print(solution.FindKthToTail({0, 2, 3, 4, 5}, 5))
