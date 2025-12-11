answerKey = "TFFT"
k = 1
max1 = 0
i, j = 0, 1
tnums = 0
fnums = 0
if answerKey[0] == 'T':
    tnums += 1
else:
    fnums += 1
if answerKey[1] == 'T':
    tnums += 1
else:
    fnums += 1
while i < len(answerKey) and j < len(answerKey) and i < j:
    s = min(tnums, fnums)
    if s <= k:
        max1 = max(max1, j - i+1)
        j += 1
        if i < len(answerKey) and j < len(answerKey) and i < j:
            if answerKey[j] == 'T':
                tnums += 1
            else:
                fnums += 1
        else:
            break
    else:
        i += 1
        if i < len(answerKey) and j < len(answerKey) and i < j:
            if answerKey[i-1] == 'T':
                tnums -= 1
            else:
                fnums -= 1
        else:
            break


def characterReplacement(s: str, k: int) -> int:
    num = [0] * 26
    # left: 左边界，用于滑动时减去头部或者计算长度
    # right: 右边界，用于加上划窗尾巴或者计算长度
    maxn = left = right = 0

    while right < len(s):
        num[ord(s[right]) - ord("A")] += 1
        # 求窗口中曾出现某字母的最大次数
        # 计算某字母出现在某窗口中的最大次数，窗口长度只能增大或者不变（注意后面left指针只移动了0 - 1次）
        # 这样做的意义：我们求的是最长，如果找不到更长的维持长度不变返回结果不受影响
        maxn = max(maxn, num[ord(s[right]) - ord("A")])
        # 长度len = right - left + 1, 以下简称len
        # len - 字母出现最大次数 > 替换数目 = > len > 字母出现最大次数 + 替换数目
        # 分析一下，替换数目是不变的 = k, 字母出现最大次数是可能变化的，因此，只有字母出现最大次数增加的情况，len才能拿到最大值
        # 又不满足条件的情况下，left和right一起移动, len不变的
        if right - left + 1 - maxn > k:
            # 这里要减的，因为left越过该点，会对最大值有影响
            num[ord(s[left]) - ord("A")] -= 1
            left += 1
        # 走完这里的时候，其实right会多走一步
        right += 1
    # 因为right多走一步，结果为(right - 1) - left + 1 == right - left
    return right - left

print(characterReplacement("TFFT",1))
print(max1)

