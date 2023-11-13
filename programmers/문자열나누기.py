def solution(s):
    same = 0
    other = 0
    answer = 0
    x = s[0]
    for i in range(len(s)):
        if s[i] == x:
            same += 1
        else:
            other += 1

        if (i == len(s) - 1):
            answer += 1
            break

        if same == other:
            answer += 1
            x = s[i + 1]
            same = 0
            other = 0

        if (i == len(s) - 1):
            answer += 1
            break

    return answer

s = input()
result = solution(s)
print(result)