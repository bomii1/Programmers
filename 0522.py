def solution(s):
    result = 0
    x = s[0]
    cnt, xcnt = 0, 1
    for i in range(1, len(s)):
        if x == s[i]:
            xcnt += 1
        else:
            cnt += 1
        if cnt == xcnt:
            result += 1
            x = s[i]
            cnt, xcnt = 0, 1
    return result
print(solution("banana"))

