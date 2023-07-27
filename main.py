num  = int(input())
satisfaction = []
for sat in range(num):
    k=int(input())
    satisfaction.append(k)
print(satisfaction)
max = len(satisfaction) + 1
nach = 1
proiz = 0
mas = []
ret = 0
for i in range(len(satisfaction)):
    for j in range(len(satisfaction)):
        if satisfaction[i] < satisfaction[j]:
            satisfaction[i], satisfaction[j] = satisfaction[j], satisfaction[i]
print(satisfaction)
for j in range(len(satisfaction)):
    for sat in range(1, max):
        proiz += satisfaction[j + sat - 1] * sat
    mas.append(proiz)
    nach += 1
    max -= 1
    proiz = 0
for find in mas:
    if find > ret:
        ret = find
print(ret)