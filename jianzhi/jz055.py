class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型
#
class Solution:
    def TreeDepth(self, pRoot: TreeNode) -> int:
        # write code here
        if pRoot is None:
            return 0
        maxleft = self.TreeDepth(pRoot.left) + 1
        maxright = self.TreeDepth(pRoot.right) + 1
        return max(maxleft, maxright)


import queue


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 空节点没有深度
        if not root:
            return 0
        # 队列维护层次后续节点
        q = queue.Queue()
        # 根入队
        q.put(root)
        # 记录深度
        res = 0
        # 层次遍历
        while not q.empty():
            # 记录当前层有多少节点
            n = q.qsize()
            # 遍历完这一层，再进入下一层
            for i in range(n):
                node = q.get()
                # 添加下一层的左右节点
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            # 深度加1
            res += 1
        return res
