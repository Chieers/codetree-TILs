num = list(map(int, input().split()))

sum = 0
count = 0
for i in range(1,len(num),2):
    sum = num[i] + sum

sum1 = 0
for i in range(2, len(num),3):
    sum1 = num[i] + sum1
    count += 1


print(sum, round(sum1/count,0))