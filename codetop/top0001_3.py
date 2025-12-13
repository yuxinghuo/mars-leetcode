class Solution:

    def lengthOfLongestSubstring1(self, s: str) -> int:
        set1 = set()
        max1 = 0
        right = -1
        for left in range(len(s)):
            if left != 0:
                set1.remove(s[left - 1])
            while right + 1 < len(s) and s[right + 1] not in set1:
                set1.add(s[right + 1])
                right = right + 1
            max1 = max(max1, right - left + 1)
        print(max1)
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

    def lengthOfLongestSubstring2(self,s:str)->int:
        if len(s) <=1:
            return 0
        if len(s) == 1:
            return 1
        set1 = set()
        max1 = 0
        left = 0
        while left < len(s):
            set1.clear()
            set1.add(s[left])
            right = left + 1
            while right < len(s) and s[right] not in set1:
                set1.add(s[right])
                right = right + 1
            max1 = max(max1, len(set1))
            left = left + 1
        print(max1)


if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLongestSubstring2("abcabcbb")
