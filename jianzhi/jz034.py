class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def FindPath(self , root: TreeNode, target: int) -> List[List[int]]:
        # write code here
        ret,path=[],[]
        def dfs(root:TreeNode,target:int):
            if not root:
                return
            path.append(root.val)
            target-=root.val
            if not root.left and not root.right and target==0:
                ret.append(path[:])
            dfs(root.left,target)
            dfs(root.right,target)
            path.pop()
        dfs(root,target)
        return ret