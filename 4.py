i = 100
k = 0
checker = True
mass = []
while not i == 1000:
    for j in range(100 + k, 1000):
        result = i * j
        req_1 = list(str(result))
        req_2 = req_1[::-1]
        if req_1 == req_2:
            mass.append(result)
    i += 1
    k += 1
print(max(mass))
    