class Solution:
    def GetNext(self, pNode):
        # 情况一
        if pNode.right:
            rchild = pNode.right
            # 一直找到右子树的最左下的结点为返回值
            while (rchild.left):
                rchild = rchild.left
            return rchild

        # 情况二
        # 如果无右子树且当前结点是其父节点的左子结点
        if pNode.next and pNode.next.left == pNode:
            return pNode.next

        # 情况三
        if pNode.next:
            ppar = pNode.next
            # 沿着左上一直爬树，爬到当前结点是其父节点的左自己结点为止
            while (ppar.next and ppar.next.right == ppar):
                ppar = ppar.next
            return ppar.next

        return None
