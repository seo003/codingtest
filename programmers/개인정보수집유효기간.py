def solution(today, terms, privacies):
    answer = []
    # today = list(map(int, today.split(".")))
    termDic = {}

    for term in terms:
        t = term.split(" ")
        termDic[t[0]] = t[1]

    for i in range(len(privacies)):
        p = str(privacies[i]).split(" ")
        priDate = list(map(int, p[0].split(".")))
        priTerm = p[1]
        if priTerm in termDic.keys():
            priDate[1] += int(termDic[priTerm])
            priDate[2] -= 1
            if priDate[1] > 12:
                addMonth = priDate[1] // 12
                priDate[1] %= 12
                priDate[0] += addMonth
            if priDate[2] == 0:
                priDate[1] -= 1
                priDate[2] = 28

        # if today[0] <= priDate[0]:
        #     if today[1] <= priDate[1]:
        #         if today[2] > priDate[2]:
        #             answer.append(i+1)
        #             print("일")
        #
        #     else:
        #         answer.append(i+1)
        #         print("월")
        # else:
        #     answer.append(i+1)
        #     print("년")

        finalDate = f"{priDate[0]}.{priDate[1]}.{priDate[2]}"
        if today >= finalDate:
            answer.append(i+1)

    return answer

today = "2016.02.15"
terms = ["A 100"]
privacies = ["2000.06.16 A", "2008.02.15 A"]


result = solution(today, terms, privacies)
print(result)