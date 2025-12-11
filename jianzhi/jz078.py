class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型二维数组
#
from typing import List

import queue


class Solution:
    def Print(self, pRoot: TreeNode) -> List[List[int]]:
        head = pRoot
        res = []
        if not head:
            # 如果是空，则直接返回空list
            return res
            # 队列存储，进行层次遍历
        temp = queue.Queue()
        temp.put(head)
        while not temp.empty():
            # 记录二叉树的某一行
            row = []
            n = temp.qsize()
            # 因先进入的是根节点，故每层节点多少，队列大小就是多少
            for i in range(n):
                p = temp.get()
                row.append(p.val)
                # 若是左右孩子存在，则存入左右孩子作为下一个层次
                if p.left:
                    temp.put(p.left)
                if p.right:
                    temp.put(p.right)
            res.append(row)
        return res
