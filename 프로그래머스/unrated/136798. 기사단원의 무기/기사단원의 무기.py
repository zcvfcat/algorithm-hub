def solution(number, limit, power):
    answer = 0

    for num in range(1, number + 1):
        cnt = 0

        for n in range(1, int(num**0.5)+1):
            if num % n == 0:
                cnt += 2

        if num ** 0.5 == int(num ** 0.5):
            cnt -= 1

        answer += cnt if cnt <= limit else power

    return answer
