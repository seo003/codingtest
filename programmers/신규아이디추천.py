def solution(new_id):
    #소문자화
    change = new_id.lower()

    #문자제거
    removeChar = "~!@#$%^&*()=+[{]}:?,<>/"
    for char in removeChar:
        if char in change:
            change = change.replace(char, '')

    while(True):
        if '..' in change:
            change = change.replace('..', '.')
        else:
            break

    #앞이나 뒤 . 제거
    if len(change) > 0:
        if change[0] == '.':
            change = change[1:]

    if len(change) > 0:
        if change[len(change)-1] == '.':
            change = change[:-1]

    #빈문자열
    if change == '':
        change = "a"

    #길이수
    if len(change) >= 16:
        change = change[:15]
        if change[len(change) - 1] == '.':
            change = change[:-1]
    elif len(change) <= 2:
        for _ in range(3-len(change)):
            change += change[-1]

    answer = change
    return answer

new_id = "=.="
print(solution(new_id))