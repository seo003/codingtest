#팔씨름
T = int(input())
for t in range(T):
    winOrLose = input()
    result = 'NO'
    wl = list(winOrLose)

    while(len(wl) < 15):
        wl.append('o')

    if wl.count('o') >= 8:
        result = 'YES'

    print(f"#{t+1} {result}")