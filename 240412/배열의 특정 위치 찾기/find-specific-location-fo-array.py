num = list(map(int, input().split()))

sum = 0
count = 0
for i in range(1,len(num),2):
    sum = num[i] + sum
    count += 1

print(sum, sum/count)