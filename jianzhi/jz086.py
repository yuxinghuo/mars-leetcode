class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    # 记录是否找到到o的路径
    flag = False

    # 求得根节点到目标节点的路径
    def dfs(self, root: TreeNode, path: List[int], o: int):
        if self.flag or not root:
            return
        path.append(root.val)
        # 节点值都不同，可以直接用值比较
        if root.val == o:
            self.flag = True
            return
        # dfs遍历查找
        self.dfs(root.left, path, o)
        self.dfs(root.right, path, o)
        # 找到
        if self.flag:
            return
        # 该子树没有，回溯
        path.pop()

    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        path1, path2 = [], []
        # 求根节点到两个节点的路径
        self.dfs(root, path1, o1)
        # 重置flag，查找下一个
        self.flag = False
        self.dfs(root, path2, o2)
        i = 0
        res = None
        # 比较两个路径，找到第一个不同的点
        while i < len(path1) and i < len(path2):
            if path1[i] == path2[i]:
                # 最后一个相同的节点就是最近公共祖先
                res = path1[i]
                i += 1
            else:
                break
        return res
