def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            add = numbers[i] + numbers[j]
            if (i == j) or (add in answer):
                continue
            answer.append(add)

    answer.sort()
    return answer

numbers = [1,2,6,10,13,20]
print(solution(numbers))