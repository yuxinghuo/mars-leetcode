if __name__ == '__main__':
    lst = input().split(" ")

    lst2 = input().split(" ")
    n = int(lst[0])
    m = int(lst[1])
    k = int(lst[2])
    lst2.sort()
    lst2.reverse()
    count1 = (m // (k + 1)) * (k * int(lst2[0]) + int(lst2[1]))
    count2 = m % (k + 1) * int(lst2[0])
    count = count1 + count2
    print(count)
