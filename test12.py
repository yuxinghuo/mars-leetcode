if __name__ == '__main__':
    lst = input().split(' ')
    n = int(lst[0])
    m = int(lst[1])
    lst_pos = list(map(int, input().split(' ')))
    lst_id = list(map(int, input().split(' ')))
    lst_ren, lst_market = [], []
    for i, idx in enumerate(lst_id):
        if idx:
            lst_market.append((lst_pos[i]))
        else:
            lst_ren.append(lst_pos[i])
    lst_ren.sort()
    i, res = 0, [0] * m
    for ren in lst_ren:
        tmp = list(map(lambda x: abs(x[0] - x[1]), zip(lst_market, [ren] * len(lst_market))))
        idx = tmp.index(min(tmp))
        res[idx] += 1
    res = [str(i) for i in res]
    print(' '.join(list(map(str, list))))
