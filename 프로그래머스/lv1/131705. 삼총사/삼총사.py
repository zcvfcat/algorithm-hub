def combinations(array, tie):
    if tie == 0:
        return [[]]

    ans = []

    for idx, node in enumerate(array):
        for edges in combinations(array[idx + 1:], tie - 1):
            ans.append([node, *edges])

    return ans


def solution(number):
    arr = list(combinations(number, 3))

    return sum([sum(a) == 0 for a in arr])
