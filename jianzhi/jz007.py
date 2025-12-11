from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reConstructBinaryTree(self, pre: List[int], vin: List[int]) -> TreeNode:
    # write code here
    if not pre or not vin:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])

    # 前序遍历的第一个元素是根节点
    root_val = pre[0]
    root = TreeNode(root_val)
    # 从中序遍历中找到根节点位置
    root_idx = vin.index(root_val)
    # 根节点左侧元素为左子树，右侧元素为右子树
    left_num = root_idx
    right_num = len(vin) - root_idx - 1
    # 递归构建左右子树
    root.left = self.reConstructBinaryTree(pre[1: left_num + 1], vin[:root_idx])
    root.right = self.reConstructBinaryTree(pre[-right_num:], vin[root_idx + 1:])
    return root


def reConstructBinaryTree1(self, pre: List[int], vin: List[int]) -> TreeNode:
    if not pre or not vin:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    # 遍历前序
    rootVal = pre[0]
    root = TreeNode(rootVal)
    index = vin.index(rootVal)
    # 根节点左侧元素为左子树，右侧元素为右子树
    left_num = index
    right_num = len(vin) - index - 1
    root.left = self.reConstructBinaryTree1(pre=pre[1:left_num + 1], vin=vin[:index])
    root.right = self.reConstructBinaryTree1(pre=pre[-right_num:], vin=vin[index + 1:])
    return root
