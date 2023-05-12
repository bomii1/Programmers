def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    today = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return today[(sum(month[:a-1]) + b) % 7]

print(solution(2,28))

