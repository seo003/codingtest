def solution(s):
    answer = False
    num = '1234567890'

    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if s[i] in num:
                answer = True
            else:
                answer = False
                break

    return answer

s = input()
result = solution(s)
print(result)