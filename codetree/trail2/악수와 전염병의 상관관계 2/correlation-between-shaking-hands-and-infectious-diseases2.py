N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

left_infection_count = [K] * (N + 1)
infected = [0] * (N + 1)
infected[P] = 1

handshakes.sort(key = lambda x : x[0])

for t, x, y in handshakes:
    x_infected, y_infected = infected[x], infected[y]
    if x_infected and left_infection_count[x]:
        infected[y] = 1
        left_infection_count[x] -= 1
    if y_infected and left_infection_count[y]:
        infected[x] = 1
        left_infection_count[y] -= 1
        
print(''.join(map(str, infected[1:])))