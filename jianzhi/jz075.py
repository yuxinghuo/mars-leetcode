# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.string = ""
        self.stringOnce = ""
        self.mp = dict()

    def FirstAppearingOnce(self):
        return self.stringOnce

    # write code here

    def Insert(self, char):
        # write code here
        self.string = self.string + char
        if self.mp.get(char) is not None:
            self.mp[char] = self.mp[char] + 1
        else:
            self.mp[char] = 1
        for i in self.string:
            if self.mp[i] == 1:
                self.stringOnce = self.stringOnce + i
                return
        self.stringOnce = self.stringOnce + "#"
