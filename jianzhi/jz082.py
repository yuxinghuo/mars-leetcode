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
# @return bool布尔型
#
class Solution:
    def dfs(self,curNode:TreeNode,target:int) ->bool:
        if not curNode:
            return False
        target -=curNode.val
        if curNode.left is None and curNode.right is None and target ==0:
            return True
        return self.dfs(curNode.left,target) or self.dfs(curNode.right,target)
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code here
        if not root:
            return False
        return self.dfs(root,sum)