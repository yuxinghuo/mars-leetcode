class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return bool布尔型
#
class Solution:
    def deep(self, root: TreeNode):
        if not root:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        return left + 1 if left > right else right + 1

    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        # write code here
        if not pRoot:
            return True
        leftnum = self.deep(pRoot.left)
        rightnum = self.deep(pRoot.right)
        if abs(leftnum - rightnum) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(
            pRoot.right
        )
