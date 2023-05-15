def solution(number, limit, power):
    divCount = [divisorCount(x) for x in range(1, number+1)]
    return sum(list(map(lambda x:power if x > limit else x, divCount)))


def divisorCount(number):
    div = []
    for i in range(1, int(number ** (0.5)) + 1):
        if number % i == 0:
            div.append(i)
            if (i ** 2) != number:
                div.append(number // i)
    return len(div)
