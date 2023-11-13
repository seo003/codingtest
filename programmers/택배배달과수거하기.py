def solution(cap, n, deliveries, pickups):
    answer = -1
    dcap = 0
    pcap = 0
    distance = 0
    for i in range(n-1, -1, -1): #i = 4,3,2,1,0
        if deliveries[i] != 0:
            dcap += deliveries[i]
            distance = i+1
            if dcap > cap:
                dcap -= deliveries[i]
                break
            deliveries[i] = 0
            print(dcap)
            print(deliveries)
            print(distance)
    return answer

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
print(solution(cap, n, deliveries, pickups))