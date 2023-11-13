def solution(emergency):
    newEmer = sorted(emergency, reverse=True)
    answer = emergency.copy()

    for i in range(len(newEmer)):
        find = emergency.index(newEmer[i])
        answer[find] = i+1

    # for var in newEmer:
    #     a = emergency.index(var) + 1
    #     print(a)

    return answer

emergency = [7, 2, 1]
print(solution(emergency))