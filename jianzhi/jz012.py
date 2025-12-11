from typing import List


def hasPath(self, matrix: List[List[str]], word: str) -> bool:
    if len(matrix) == 0:
        return False
    n = len(matrix)
    m = len(matrix[0])
    # 初始化flag矩阵记录是否走过
    flag = [[False for i in range(m)] for j in range(n)]
    # 遍历矩阵找起点
    for i in range(n):
        for j in range(m):
            if dfs(matrix=matrix, n=n, m=m, i=i, j=j, word=word, k=0, flag=flag):
                return True
    return False


def dfs(matrix: List[List[str]], n: int, m: int, i: int, j: int, word: str, k: int,
        flag: List[List[bool]]) -> bool:
    if i < 0 or i >= n or j < 0 or j >= m or (matrix[i][j] != word[k]) or flag[i][j]:
        return False
    if k == len(word) - 1:
        return True
    flag[i][j] = True
    # 该节点任意方向出发：
    if (dfs(matrix, n, m, i - 1, j, word, k + 1, flag)
            or dfs(matrix, n, m, i + 1, j, word, k + 1, flag)
            or dfs(matrix, n, m, i, j + 1, word, k + 1, flag)
            or dfs(matrix, n, m, i, j - 1, word, k + 1, flag)):
        return True
    flag[i][j] = False
    return False


print(hasPath(self=None, matrix=[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word='ABCB'))
