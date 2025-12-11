from typing import List


class Solution:
    def movingCount(self, threshold: int, rows: int, cols: int) -> int:
        # write code here
        return self.dfs(rows=rows, cols=cols, i=0, j=0, threshold=threshold)

    def dfs(self, rows: int, cols: int, i: int, j: int, threshold: int) -> int:
        if i <= rows and j <= cols and self.ifTrue(i, j, threshold):
            count = 1
            if self.dfs(rows=rows, cols=cols, i=i + 1, j=j, threshold=threshold) > 0:
                count += count
            if self.dfs(rows=rows, cols=cols, i=i, j=j + 1, threshold=threshold) > 0:
                count += count
            return count
        else:
            return 0

    def ifTrue(self, i: int, j: int, threshold: int) -> bool:
        sum = 0
        while i > 0:
            sum += i % 10
            i = i // 10
        while j > 0:
            sum += j % 10
            j = j // 10
        if sum <= threshold:
            return True
        else:
            return False
