def solution(plans):
    answer = []
    
    for i,v in enumerate(plans): # 시간 문자열을 숫자로 변경
        job, t1, t2 = v
        hh,mm = t1.split(":")
        plans[i][1],plans[i][2] = int(hh) * 60 + int(mm), int(t2)

    plans.sort(key=lambda x:x[1]) # 정렬
        
    stack = [] # 스택 초기화
    stack.append(plans[0]) # 스택에 작업 넣기
    
    time = plans[0][1] # 첫 작업 시작 시간
    
    for i in range(1, len(plans)):
        next_time = plans[i][1] # 다음 작업 시작 시간

        while len(stack): # 스택에 작업이 있으면
            job, time_start, time_spend = stack.pop() # 스택에서 작업 꺼내기
            
            if time < time_start: # 현재 시간보다 스택에 있는 작업 시작 시간이 느리면
                time = time_start # 시간 조정
                
            time_finish = time + time_spend # 스택의 작업이 끝나는 시간

            if next_time < time_finish: # 다음 작업 시작 시간이 스택에 있는 작업 완료시간보다 빠르면 
                stack.append([job, time_start, time_finish - next_time]) # 스택에서 꺼낸 작업을 다시 넣고
                time = next_time # 현재 시간은 다음 작업 시작 시간으로 변경
                break # 중지
            else:
                answer.append(job) # 스택의 작업을 완료한다.
                time += time_spend # 현재 시간에 소요 시간을 더한다.
                                   # 스택에 작업이 있으면 계속

        stack.append(plans[i]) # 스택에 작업 넣기

    while len(stack): # 스택에 남은 작업 꺼내서 완료하기
        answer.append(stack.pop()[0])

    return answer