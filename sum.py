def add(N):
    sum = 0
    for i in range(1,N+1):
        sum += i
    return sum
Num = int(input())
print(add(Num))