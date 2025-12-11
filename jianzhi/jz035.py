# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def Clone(self, pHead):
        #空节点直接返回
        if pHead is None:
            return pHead
        #添加一个头部节点
        res = RandomListNode(0)
        #哈希表，key为原始链表的节点，value为拷贝链表的节点
        mp = dict()
        cur = pHead
        pre = res
        #遍历原始链表，开始复制
        while cur is not None:
            #拷贝节点
            clone = RandomListNode(cur.label)
            #用哈希表记录该节点下的拷贝节点
            mp[cur] = clone
            #连接
            pre.next = clone
            pre = pre.next
            #遍历
            cur = cur.next
        #遍历哈希表
        for (key, value) in mp.items():
            #原始链表中random为空
            if key.random is None:
                value.random = None
            else:
                #将新链表的random指向哈希表中原始链表的random
                value.random = mp[key.random]
        #返回去掉头
        return res.next
