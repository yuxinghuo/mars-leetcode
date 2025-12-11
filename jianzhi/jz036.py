class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    head = None
    pre = None
    def Convert(self, pRootOfTree: TreeNode):
        if not pRootOfTree:
            # 中序递归，叶子为空则返回
            return None
        # 首先递归到最左最小值
        self.Convert(pRootOfTree.left)
        # 找到最小值，初始化head与pre
        if not self.pre:
            self.head = pRootOfTree
            self.pre = pRootOfTree
        # 当前节点与上一节点建立连接，将pre设置为当前值
        else:
            self.pre.right = pRootOfTree
            pRootOfTree.left = self.pre
            self.pre = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.head
