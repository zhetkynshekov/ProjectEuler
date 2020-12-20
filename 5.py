import time

startTime = time.time()
checker = True
num = 20
mass = []
k = 0
while checker == True:
    for i in range(1,21):
        if num % i == 0:
            k += 1
            if k == 20:
                totalTime = round(time.time() - startTime, 2)
                print(str(num) + " Время выполнения:" + str(totalTime))
                checker = False
    k = 0
    num += 20