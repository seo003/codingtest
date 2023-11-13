def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer

arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))