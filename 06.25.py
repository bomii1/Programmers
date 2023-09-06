def solution(s, skip, index):
    s = list(s)
    for i in range(len(s)):
        count = 0
        for j in range(index):
            for k in range(len(skip)):
                if chr(ord(s[i])+j+1) == skip[k]:

                    count += 1
        index_s = ord(s[i]) + index + count
        if index_s > 122:
            index_s -= 26
        s[i] = chr(index_s)
    return "".join(s)






s = "zzzzz"
skip = "a"
print(solution(s, skip, 1))


