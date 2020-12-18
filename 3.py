mass = []
n = 600851475143
z = 2
while z * z <= n:
    if n % z == 0:
        mass.append(z)
        z += 1
    else:
        z += 1
k = 0
mass_2 = []
for item in mass:
    for j in range(1,item + 1):
        if item % j == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        mass_2.append(int(item))
    k = 0
print(max(mass_2))