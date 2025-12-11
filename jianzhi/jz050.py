#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return int整型
#
class Solution:
    def FirstNotRepeatingChar(self, str: str) -> int:
        # write code here
        mp = dict()
        for i in str:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for i in range(len(str)):
            if mp[str[i]] == 1:
                return i
        return -1
