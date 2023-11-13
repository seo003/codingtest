def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(eng)):
        if eng[i] in s:
            s = s.replace(eng[i], str(i))

    answer = int(s)
    return answer

s = input()
result = solution(s)
print(result)