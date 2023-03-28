from heapq import heappush, heappop


def solution(k, score):
    answer = []
    heap = []

    for s in score:
        heappush(heap, s)

        if len(heap) > k:
            heappop(heap)

        answer.append(heap[0])

    return answer