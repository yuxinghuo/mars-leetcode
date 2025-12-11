from typing import List
import collections
list1 = [4, 3, 1, 1, 3, 3, 2]
# list1 = [5,5,4]
k = 3
dict1 = {}
for i in list1:
    if dict1.get(i):
        dict1[i] = (dict1.get(i) + 1)
    else:
        dict1[i] = 1
while k > 0:
    min1 = -1
    for i in dict1.keys():
        if min1 == -1:
            min1 = dict1.get(i)
            minkey = i
        if dict1.get(i) < min1:
            min1 = min(min1, dict1.get(i))
            minkey = i
    k = k - dict1.get(minkey)
    # list1 = list(filter(lambda x: x != minkey, list1))
    dict1.pop(minkey)
if k < 0:
    print(len(dict1.keys()) + 1)
else:
    print(len(dict1.keys()))



class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        group = collections.Counter(arr)
        print(type(group))
        c=dict(group)
        a=group.most_common()
        freq = group.most_common()[::-1]
        ans = len(freq)
        for _, occ in freq:
            if k >= occ:
                ans -= 1
                k -= occ
            else:
                break
        return ans


solution=Solution()
a=solution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2],k = 3)
print(a)




