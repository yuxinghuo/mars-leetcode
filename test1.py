def gerAllStr(s: str):
    list = []
    for i in s:
        if i == "]":
            curStr = ""
            va = list.pop()
            flag = 0
            while flag == 0 or (flag == 1 and va.isnumeric()):
                if va == "[":
                    flag = 1
                curStr = curStr + va
                if len(list) != 0:
                    va = list.pop()
                else:
                    break
            if va.isnumeric() == False and len(list) != 0:
                list.append(va)
            curStr = curStr[::-1]
            num, str1 = curStr.split('[')[0], curStr.split('[')[1]
            str2 = str1 * int(num)
            for j in range(len(str2)):
                list.append(str2[j])
        else:
            list.append(i)
    return ''.join(list)

print(gerAllStr("3[m]2[n]"))
