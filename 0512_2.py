# 1: 빵, 2: 야채, 3: 고기 -> [1,2,3,1]

"""
def dp(ingredient):
    hmbg = "1231"
    dp = [[0 for j in range(len(hmbg)+1)] for i in range(len(ingredient)+1)]

    for i in range(1, len(ingredient)+1):
        for j in range(1, len(hmbg)+1):
            if str(ingredient[i-1]) != hmbg[j-1]:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j-1] + 1
    return dp[-1][-1]
print(dp([2, 1, 1, 2, 3, 1, 2, 3, 1]))
"""

def success(ingredient):
    ham = [1,2,3,1]
    cnt = 0
    for i in range(len(ingredient)):
        if cnt > 3:
            return ingredient
        if ingredient[i] == ham[cnt]:
            cnt += 1
            ingredient.remove(ingredient[i])
    return ingredient


print(success([2, 1, 1, 2, 3, 1, 2, 3, 1]))

