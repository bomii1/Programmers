def solution(s):
    result = 0
    x = s[0]
    cnt, xcnt = 0, 1
    for i in range(1, len(s)):
        if len(s[i:]) <= 1:
            return result + 1 if len(s[i:]) == 1 else result
        if x == s[i]:
            xcnt += 1
        else:
            cnt += 1
        if cnt == xcnt:
            result += 1
            if len(s[i+1:]) > 1:
                if len(s[i+1:]) == 2:
                    return result + 1
                else:
                    print(s[i+1:])
                    return solution(s[i+1:]) + result
    return 1

