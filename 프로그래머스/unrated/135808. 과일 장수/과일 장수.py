def solution(k, m, score: list):
    score.sort(reverse=True)

    total = 0
    for i in range(0, len(score), m):
        sliced = score[i: i + m]

        if len(sliced) == m:
            total += min(sliced) * m
    return total
