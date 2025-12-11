class Solution(object):
    def Permutation(self, ss):
        n = len(ss)
        if n <= 1:  # 递归边界，空串或者一个字符
            return ss
        lst = []
        for i in range(n):
            s1 = ss[i]
            for s2 in self.Permutation(ss[:i] + ss[i + 1:]):  # 递归搜索，不取ss[i]
                new_str = s1 + s2  # s1和s2拼接成新的排序
                if new_str not in lst:  # 如果当前没有这个排序
                    lst.append(new_str)
        lst = sorted(lst)  # 字典序，从小到大排序
        return lst


str = "ads"
solution = Solution()
solution.Permutation(ss=str)
