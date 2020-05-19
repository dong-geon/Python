N = int(input())
cnt = 0
while N > 0:
    if N % 5 != 0:
        N -= 3
        if N < 0:
            cnt = -1
            break
        cnt += 1
    elif N % 5 == 0:
        N -= 5
        cnt += 1
    elif N % 5 != 0 and N % 3 != 0:
        cnt = -1
        break

print(cnt)
