def solution(s):
    answer = []
    
    for i, c in enumerate(s):
        for j in range(i - 1, -1, -1):
            if s[j] == c:
                answer.append(i - j)
                break
        else:
             answer.append(-1)   
        
        
    print('asdas')
    return answer