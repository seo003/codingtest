def solution(babbling):
    voiceList = ['aya', 'ye', 'woo', 'ma']
    answer = 0

    for bab in babbling:
        for voice in voiceList:
            if voice in bab:
                if voice*2 in bab:
                    continue
                bab = bab.replace(voice, ' ')
                if all(b == ' ' for b in bab):
                    answer += 1

    return answer

babbling = ["yayae"]
result = solution(babbling)
print(result)