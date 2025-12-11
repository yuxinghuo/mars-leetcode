#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # write code here
        i, j = 0, 0
        mp = dict()
        max1 = 0
        while j < len(s):
            if s[j] in mp:
                mp[s[j]] += 1
            else:
                mp[s[j]] = 1
            # 出现次数大于1，则窗口内有重复
            while mp[s[j]] > 1:
                # 窗口左移，同时减去该字符的出现次数
                mp[s[i]] -= 1
                i += 1
            # 维护子串长度最大值
            max1 = max(max1, j - i + 1)
            j += 1
        return max1


solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")
