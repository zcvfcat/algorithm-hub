from heapq import heappush, heappop


def solution(book_time):
    answer = 1

    time = [(int(start[:2]) * 60 + int(start[3:]), int(end[:2]) * 60 + int(end[3:])) for start, end in book_time]
    sorted_time = sorted(time)
    q = []

    for start, end in sorted_time:
        if not q:
            heappush(q, end)
            continue
        
        if q[0] <= start:
            heappop(q)
        else:
            answer += 1
        
        heappush(q, end + 10)

    return answer



print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
