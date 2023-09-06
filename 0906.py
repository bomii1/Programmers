def solution(numbers):
    newNumArr = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            newNumArr.append(numbers[i] + numbers[j])
    return sorted(list(set(newNumArr)))

x = solution([2,1,3,4,1])
print(x)