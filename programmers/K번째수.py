def solution(array, commands):
    answer = []

    for command in commands:
        start = command[0]
        end = command[1]
        th = command[2]

        newArray = array[start-1:end]
        newArray.sort()
        answer.append(newArray[th-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))