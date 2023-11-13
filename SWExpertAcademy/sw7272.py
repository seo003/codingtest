#안경이 없어!
T = int(input())
for t in range(T):
    compare = input().split()
    Left = list(compare[0])
    Right = list(compare[1])
    if len(Left) != len(Right):
        print(f"#{t+1} DIFF")
        continue
    result = ''
    for left in Left:
        for right in Right:
            if left in 'CEFGHIJKLMNSTUVWXYZ' and right in 'CEFGHIJKLMNSTUVWXYZ':
                result = 'SAME'
            elif left in 'ADOPQR' and right in 'ADOPQR':
                result = 'SAME'
            elif left == 'B' and right == 'B':
                result = 'SAME'
            else:
                result = 'DIFF'
    print(f"#{t+1} {result}")