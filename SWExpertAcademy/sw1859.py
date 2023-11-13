#백만장자 프로젝트
T = int(input())
for i in range(T):
    N = int(input())
    prices = input().split()
    #prices = list(map(int, input().split())) -> int로 변경되서 리스트에 저장

    profit = 0 #이익
    max = int(prices[N-1]) #마지막거...
    # 뒤에부터 하나씩 확인해서...
    for j in range(N-1, 0, -1):
        # 앞에꺼가 작으면
        if int(prices[j]) >= int(prices[j-1]):
            # 뒤에꺼에서 앞에꺼 빼서 profit에 저장
            # 이때 뒤에 더 큰게 있으면 거기서 빼기....
            if max != int(prices[j]):
                profit += max - int(prices[j - 1])
                continue
            max = int(prices[j])
            profit += max - int(prices[j - 1])
        #앞에가 크면
        else :
            if prices[j-1] != prices[0]:
                max = int(prices[j-1])

    print(f"#{i+1} {profit}")


