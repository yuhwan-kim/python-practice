# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

x = a * b * c
xtr = str(x)

counts = [0] * 10

for i in xtr:
    num = int(i)
    counts[num] = counts[num] + 1

for i in counts:
    print(i)