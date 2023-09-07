def solution(code):
    mode = True
    ret = ''
    for idx, val in enumerate(code):
        if mode:
            # mode = 0
            if val != '1' and idx % 2 == 0:
                ret = ret + val
            elif val == '1':
                mode = False         
        else:
            # mode = 1
            if val != '1' and idx % 2 != 0:
                ret = ret + val
            elif val == '1':
                mode = True
    if len(ret) == 0:
        return 'EMPTY'            
    return ret