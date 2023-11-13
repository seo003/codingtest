def solution(M, N):
    answer = 0
    for _ in range(M-1):
        answer += 1
    for _ in range(M):
        for _ in range(N-1):
            answer += 1
    return answer

M = 2
N = 5
print(solution(M, N))