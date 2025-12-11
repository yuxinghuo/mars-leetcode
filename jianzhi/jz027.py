class Solution:
    def Mirror(self, pRoot):
        # write code here
        if not pRoot:
            return pRoot
        # 左右子树交换
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        # 递归左右子树
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)

        return pRoot