def solution(name, yearning, photo):
    answer = []
    hashed_info = dict(zip(name, yearning))

    for people in photo:
        score = 0

        for person in people:
            score += hashed_info.get(person, 0)
        
        answer.append(score)
    
    return answer
