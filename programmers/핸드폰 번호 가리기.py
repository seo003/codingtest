def solution(phone_number):
    last_four_digits = phone_number[-4:]
    changeNum = len(phone_number)-4
    answer = "*"*changeNum + last_four_digits
    return answer

print(solution("12345687578"))