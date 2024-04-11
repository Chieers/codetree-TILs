num = list(map(int, input().split()))

SUM = 0
for i in range(0,len(num)):
    if num[i] == 0:
        SUM = num[i-3] + num[i-2] + num[i-1]
        break
print(SUM)