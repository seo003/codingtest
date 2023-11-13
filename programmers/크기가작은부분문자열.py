def solution(t, p):
    answer = 0
    pLen = len(p)

    for i in range(len(t)+1-pLen):
        compare = ""
        for j in range(pLen):
            compare += t[i+j]
        if compare <= p:
            answer += 1

    return answer

t = "500220839878"
p = "7"
print(solution(t, p))