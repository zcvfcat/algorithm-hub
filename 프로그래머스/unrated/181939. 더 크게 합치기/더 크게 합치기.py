def solution(a, b):
    a = str(a)
    b = str(b)
    return int(a + b) if a + b > b + a else int(b + a)