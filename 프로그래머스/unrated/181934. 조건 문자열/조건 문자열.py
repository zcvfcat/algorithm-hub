def solution(ineq, eq, n, m):
    s = str(n) + ineq + eq.replace('!','') + str(m)
    print(s)
    # eval을 쓰다니;;
    ans = int(eval(s))
    return ans