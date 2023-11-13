#둘만의 암호
def isnotalpa(next):
    if next == chr(ord("z") + 1):
        return True
    return False

def solution(s, skip, index):
    answer = ''
    for sChange in s:
        char_list = []
        next = sChange
        count = 0

        while count < index:
            next = chr(ord(next) + 1)
            if isnotalpa(next):
                next = "a"
            char_list.append(next)
            count += 1

        while any(char in skip for char in char_list):
            for char in char_list:
                if char in skip:
                    char_list.remove(char)
                    count -= 1

            if count != index:
                for _ in range(index - count):
                    next = chr(ord(next) +1)
                    if isnotalpa(next):
                        next = "a"
                    char_list.append(next)
                    count +=1

        answer += char_list.pop()
    return answer

s, skip, index = input().split()
result = solution(s, skip, int(index))
print(result)
