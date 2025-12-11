class Solution:
    def __init__(self) -> None:
        self.list1 = []

    def Insert(self, num):
        self.list1.append(num)
        self.list1 = sorted(self.list1)

    # write code here
    def GetMedian(self):
        n = len(self.list1)
        if n % 2 == 0:
            return (self.list1[n // 2] + self.list1[n // 2 - 1]) / 2
        else:
            return self.list1[n // 2]
