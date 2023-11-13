def solution(numlist, n):
    answer = []
    disDic = {}
    numlist.sort()

    for num in numlist:
        if num <= n:
            disDic[n - num] = num
        elif num > n:
            if num - n in disDic:
                disDic[num - n] = [disDic[num - n]]
                disDic[num - n].append(num)
                continue
            disDic[num - n] = num

    newDic = dict(sorted(disDic.items()))

    for values in newDic.values():
        if isinstance(values, list):
            newVal = sorted(values, reverse=True)
            for value in newVal:
                answer.append(value)
            continue

        answer.append(values)

    return answer

numlist = [10000,20,36,47,40,6,10,7000]
n = 30
print(solution(numlist, n))