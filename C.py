sum=0
min=100
list=[]
for i in range(7):
    N=int(input())
    if N%2==1:
        sum += N
        list.append(N)
        if N < min:
            min=N
if len(list)==0:
    print(-1)
else:
    print(sum)
    print(min)
