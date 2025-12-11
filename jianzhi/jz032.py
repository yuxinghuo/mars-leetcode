class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#
from typing import List

import queue


class Solution:
    def PrintFromTopToBottom(self, root: TreeNode) -> List[int]:
        # write code here
        res = []
        temp = queue.Queue()
        if not root:
            return res
        temp.put(root)
        while not temp.empty():
            cur=temp.get();
            res.append(cur.val)
            if cur.left:
                temp.put(cur.left)
            if cur.right:
                temp.put(cur.right)

        return res
