#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @param k int整型
# @return int整型
#
from typing import List
class Solution:
    def bisearch(self,data:List[int],k:int):
        left, right = 0, len(data) - 1
        while left <= right:
            mid = (right + left) // 2
            if data[mid] < k:
                left = mid+1
            else:
                right = mid - 1
        return left
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        return self.bisearch(data,k+0.5)-self.bisearch(data,k-0.5)

