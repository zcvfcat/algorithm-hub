def solution(n):
    if n % 2 == 1:
        k = [i for i in range(n, - 1, - 2)]
        return sum(k)
    else:
        k = [i * i for i in range(n, - 1, - 2)]
        return sum(k)