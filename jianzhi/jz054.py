class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param proot TreeNode类
# @param k int整型
# @return int整型
#
class Solution:
    def __init__(self):
        # 记录返回的节点
        self.res = None
        # 记录中序遍历了多少个
        self.count = 0

    def midOrder(self, root, k):
        # 当遍历到节点为空或者超过k时，返回
        if not root or self.count > k:
            return
        self.midOrder(root.left, k)
        self.count += 1
        # 只记录第k个
        if self.count == k:
            self.res = root
        self.midOrder(root.right, k)

    def KthNode(self, proot: TreeNode, k: int) -> int:
        self.midOrder(proot, k)
        if self.res:
            return self.res.val
        # 二叉树为空，或是找不到
        else:
            return -1
