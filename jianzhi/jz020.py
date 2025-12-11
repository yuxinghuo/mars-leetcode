class Solution:
    def isNumeric(self, str):
        # write code here
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. start with 'blank'
            {'d': 2, '.': 4},  # 1. 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},  # 3. 'digit' after 'dot'
            {'d': 3},  # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            {'s': 6, 'd': 7},  # 5. 'e'
            {'d': 7},  # 6. 'sign' after 'e'
            {'d': 7, ' ': 8},  # 7. 'digit' after 'e'
            {' ': 8}  # 8. end with 'blank'
        ]
        p = 0  # start with state 0
        for c in str:
            if '0' <= c <= '9':
                t = 'd'  # digit
            elif c in "+-":
                t = 's'  # sign
            elif c in "eE":
                t = 'e'  # e&nbs***bsp;E
            elif c in ". ":
                t = c  # dot, blank
            else:
                t = '?'  # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)


class Solution:
    def __init__(self):
        # 遍历字符串的下标
        self.index = 0

    # 有符号判断
    def integer(self, s: str) -> bool:
        if self.index < len(s) and (s[self.index] == '-' or s[self.index] == '+'):
            self.index += 1
        return self.unsigned_integer(s)

    # 无符号数判断
    def unsigned_integer(self, s: str) -> bool:
        temp = self.index
        while self.index < len(s) and (s[self.index] >= '0' and s[self.index] <= '9'):
            self.index += 1
        return self.index > temp

    def isNumeric(self, str: str) -> bool:
        # 先判断空串
        if len(str) == 0:
            return False
        # 去除前面的空格
        while self.index < len(str) and str[self.index] == ' ':
            self.index += 1
        n = len(str) - 1
        # 去除字符串后面的空格
        while n >= 0 and str[n] == ' ':
            n -= 1
        # 限制的长度比下标1
        n += 1
        # 全是空格情况
        if n < self.index:
            return False
        # 判断前面的字符是否是有符号的整数
        flag = self.integer(str)
        # 如果有小数点
        if self.index < n and str[self.index] == '.':
            self.index += 1
            # 小数点前后有无数字可选
            flag = self.unsigned_integer(str) or flag
        # 如果有e
        if self.index < n and (str[self.index] == 'e' or str[self.index] == 'E'):
            self.index += 1
            # e后面必须全是整数
            flag = flag and self.integer(str)
        # 是否字符串遍历结束
        return flag and (self.index == n)
