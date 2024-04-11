num = list(map(int, input().split()))

even = 0
odd = 0

for i in range(0,len(num)):
    if i%2 == 0:
        odd = num[i] + odd
    elif i%2 == 1:
        even = num[i] + even
    
print(abs(odd-even))