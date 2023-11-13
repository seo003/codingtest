def solution(s):
    new = ""
    zeroCount = 0
    binaryCount = 0
    while(True):
        for i in range(len(s)):
            if s[i] == "0":
                zeroCount += 1
            elif s[i] == "1":
                new = new + "1"

        length = len(new)
        s = bin(length)[2:]
        binaryCount += 1
        if s == "1":
            break

        new = ""

    answer = [binaryCount, zeroCount]
    return answer

s = input()
result = solution(s)
print(result)