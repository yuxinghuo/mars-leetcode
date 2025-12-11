#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param base double浮点型
# @param exponent int整型
# @return double浮点型
#
class Solution:
    def Power(self , base: float, exponent: int) -> float:
        # write code here
        if exponent<0:
            base=1/base
            exponent=-exponent
        res=1.0
        for i in range(exponent):
            res *=base
        return res