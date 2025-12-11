class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param sum int整型
# @return int整型
#
class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, curNode: TreeNode, target: int):
        if not curNode:
            return
        target -= curNode.val
        if target == 0:
            self.count += 1
        self.dfs(curNode.left, target)
        self.dfs(curNode.right, target)

    def FindPath(self, root: TreeNode, sum: int) -> int:
        # write code here
        if not root:
            return 0
        self.dfs(root, sum)
        self.FindPath(root.left,sum)
        self.FindPath(root.right,sum)
        return self.count


class Solution:
    def __init__(self):
        # 记录路径和及条数
        self.mp = dict()

    # last为到上一层为止的累加和
    def dfs(self, root: TreeNode, sum: int, last: int) -> int:
        # 空结点直接返回
        if root is None:
            return 0
        res = 0
        # 到目前结点为止的累加和
        temp = root.val + last;
        # 如果该累加和减去sum在哈希表中出现过，相当于减去前面的分支
        if (temp - sum) in self.mp:
            # 加上有的路径数
            res += self.mp[temp - sum]
            # 增加该次路径和
        if temp in self.mp:
            self.mp[temp] += 1
        else:
            self.mp[temp] = 1
            # 进入子结点
        res += self.dfs(root.left, sum, temp)
        res += self.dfs(root.right, sum, temp)
        # 回退该路径和，因为别的树枝不需要这边存的路径和
        self.mp[temp] -= 1
        return res

    def FindPath(self, root: TreeNode, sum: int) -> int:
        # 路径和为0的有1条
        self.mp[0] = 1
        return self.dfs(root, sum, 0)

