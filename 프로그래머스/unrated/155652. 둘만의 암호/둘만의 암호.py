def solution(s, skip, index):
    answer = ''.join([chr(alpha) for alpha in range(ord('a'), ord('z') + 1)])
    result = []

    for i in skip:
        if i in answer:
            answer = answer.replace(i, "")

    for j in s:
        result.append(answer[(answer.index(j) + index) % len(answer)])

    return "".join(result)
