#쇠막대기 자르기
T = int(input())
for t in range(T):
    position = input()
    count = 0
    result = 0
    # for p in range(len(position)-1):
    #     if position[p] == "(":
    #         if position[p+1] == ")":
    #             result += count
    #             continue
    #         elif position[p+1] == "(":
    #             count += 1
    #             continue
    #     elif position[p] == ")":
    #         result += count
    #         count -= 1
    #         if position[p+1] == ")":
    #             continue
    #         elif position[p+1] == "(":
    #             count += 1
    #             continue

    for p in range(len(position)):
        if position[p] == "(":
            count += 1
        else:
            count -= 1
            if position[p-1] == "(":
                result += count
            else:
                result += 1


    print(f"#{t+1} {result}")