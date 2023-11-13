#공과 잡초
T = int(input())
for t in range(T):
    ground = input()
    result = 0

    for g in range(len(ground)-1):
        if ground[g] == '(' and ground[g + 1] == ')':
            result += 1
        if ground[g] == '(' and ground[g + 1] == '|':
            result += 1
        if ground[g] == '|' and ground[g + 1] == ')':
            result += 1

    print(f"#{t+1} {result}")