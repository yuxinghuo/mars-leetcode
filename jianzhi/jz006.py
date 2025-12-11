from typing import List


# JZ6 从尾到头打印链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printListFromTailToHead(self, listNode: ListNode) -> List[int]:
    alist = []
    while listNode is not None:
        alist.append(listNode.val)
        listNode = listNode.next
    alist.reverse()
    return alist


if __name__ == '__main__':
    numbers=[1, 2, 4, 7, 3, 2, 1, 4]
    numbers.reverse()
    print(numbers)
