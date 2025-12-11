class Solution:

    def lengthOfLongestSubstring1(self, s: str) -> int:
        set1 = set()
        max1 = 0
        right = -1
        for left in range(len(s)):
            if left != 0:
                set1.remove(s[left - 1])
            while s[right + 1] < len(s) and s[right + 1] not in set1:
                set1.add(s[right + 1])
                right = right + 1
            max1 = max(max1, right - left + 1)
        return max1




























    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        mp = dict()
        max1 = 0
        while j < len(s):
            if s[j] in mp:
                mp[s[j]] += 1
            else:
                mp[s[j]] = 1
            while mp[s[j]] > 1:
                mp[s[i]] -= 1
                i += 1
            max1 = max(max1, j - i + 1)
            j += 1
        return max1


solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")
