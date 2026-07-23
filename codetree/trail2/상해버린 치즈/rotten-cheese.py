from collections import defaultdict
N, M, D, S = map(int, input().split())

consume_history = [[] for _ in range(101)]
for _ in range(D):
    person, cheese, time = map(int, input().split())
    consume_history[time].append((person, cheese))

sick_history = [[] for _ in range(102)]
for _ in range(S):
    person, time = map(int, input().split())
    sick_history[time].append(person)

bad_cheeses = [] 
for bad_cheese in range(1, M + 1):
    for time, sick_persones in enumerate(sick_history):
        consume = set()
        for sick_p in sick_persones:
            for histories in consume_history[:time]:
                for h in histories:
                    consume.add(h)
        
        for sick_p in sick_persones:
            if (sick_p, bad_cheese) not in consume:
                break
    else:
        bad_cheeses.append(bad_cheese)

d = defaultdict(int)
for consumes in consume_history:
    for person, cheese in consumes:
        if cheese in bad_cheeses:
            d[cheese] += 1

print(max(d.values()))
