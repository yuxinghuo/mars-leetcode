#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def NumberOf1(self , n: int) -> int:
        res = 0
        #遍历32位
        for i in range(32):
            #按位比较
            if (n & (1 << i)) != 0:
                res += 1
        return res
