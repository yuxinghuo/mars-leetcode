class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def getPath(self, root: TreeNode, target: int) -> List[int]:
        path = []
        node = root
        # 节点值都不同，可以直接用值比较
        while node.val != target:
            path.append(node.val)
            # 小的在左子树
            if target < node.val:
                node = node.left
            # 大的在右子树
            else:
                node = node.right
        path.append(node.val)
        return path

    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        # 求根节点到两个节点的路径
        path_p = self.getPath(root, p)
        path_q = self.getPath(root, q)
        # 比较两个路径，找到第一个不同的点
        i = 0
        while i < len(path_p) and i < len(path_q):
            if path_p[i] == path_q[i]:
                # 最后一个相同的节点就是最近公共祖先
                res = path_p[i];
                i += 1
            else:
                break
        return res

    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        # 空树找不到公共祖先
        if not root:
            return -1
        # pq在该节点两边说明这就是最近公共祖先
        if (p >= root.val and q <= root.val) or (p <= root.val and q >= root.val):
            return root.val
        # pq都在该节点的左边
        elif p <= root.val and q <= root.val:
            # 进入左子树
            return self.lowestCommonAncestor(root.left, p, q)
            # pq都在该节点的右边
        else:
            # 进入右子树
            return self.lowestCommonAncestor(root.right, p, q)
