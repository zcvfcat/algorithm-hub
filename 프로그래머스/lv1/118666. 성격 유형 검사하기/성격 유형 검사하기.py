def solution(surveys, choices):
    d = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for survey, choice in zip(surveys, choices):
        if choice > 4:
            d[survey[1]] += choice - 4
        elif choice < 4:
            d[survey[0]] += 4 - choice

    l = [*d.items()]

    answer = ''
    for i in range(0, 8, 2):
        if l[i][1] < l[i + 1][1]:
            answer += l[i + 1][0]
        else:
            answer += l[i][0]

    return answer
