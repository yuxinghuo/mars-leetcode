#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @param pattern string字符串 
# @return bool布尔型
#
class Solution:
    def match(self , str , pattern ):
        m, n = len(str), len(pattern)   # 分别找到str和pattern的长度

        def matches(i, j):              #定义一个转移方程函数
            if i == 0:                  #首先考虑一种特殊情况： str为空；
           #否则第一种是当i、j指向的字符是同一个字母/点号（"."）的时候，我们只需要判断对应位置的字符是否相同，
           #相同则转移状态去判断子问题f[i-1][j-1]是否匹配
                return False
            if pattern[j - 1] == '.':
                return True
            return str[i - 1] == pattern[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True             #动态规划的边界条件为f[0][0]=true，即两个空字符串是可以匹配的
        for i in range(m + 1):
            for j in range(1, n + 1):
                #判断当j 指向 * 号的时候两种情况：
                if pattern[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]