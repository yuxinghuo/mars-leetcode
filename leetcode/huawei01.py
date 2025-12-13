def huaweilianxuzimulength(s: str, k: int) -> int:
    # 初始化26个字母的计数器
    counts = [0] * 26

    if not s:  # 处理空字符串情况
        return 0

    left = 0
    right = 1

    while left < len(s) and right <= len(s):
        if right < len(s) and s[left] == s[right]:
            right += 1
        else:
            char_index = ord(s[left]) - ord('A')
            current_length = right - left
            if current_length > counts[char_index]:
                counts[char_index] = current_length
            left = right
            right += 1

    # 降序排序并返回第k大的值
    counts.sort(reverse=True)

    # 处理k超出范围的情况
    if k > len(counts):
        return 0
    return counts[k - 1]


# 测试
print(huaweilianxuzimulength("ABC", 1))  # 输出应为1
print(huaweilianxuzimulength("AABBBCC", 2))  # 输出应为2
print(huaweilianxuzimulength("AAABBBCCC", 1))  # 输出应为3
