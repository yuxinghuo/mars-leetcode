from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        map1 = dict()
        for i in s:
            if i not in map1:
                map1[i] = 0
            map1[i] = map1[i] + 1
        a1, a2 = 0, len(s)
        for value in map1.values():
            if value % 2 :
                a1 = max(a1, value)
            else:
                a2 = min(a2, value)
        return a1 - a2
        # c = Counter(s)
        # maxOdd = max(x for x in c.values() if x % 2 == 1)
        # minEven = min(x for x in c.values() if x % 2 == 0)
        # return maxOdd - minEven
        return

    def maxDifference1(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven
