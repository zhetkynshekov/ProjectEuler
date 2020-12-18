checker = True
first = 1
second = 2
result = 2
while checker == True:
    third = first + second
    if third % 2 == 0:  
        if second > 4000000:
            checker = False
        else:
            result+=third
    first = second
    second = third
print(result)