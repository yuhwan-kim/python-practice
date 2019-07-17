# https://www.acmicpc.net/problem/10039

scores = []

for i in range(5):
    num = int(input())
    if num <= 40:
        num = 40
    scores.append(num)

sum = 0
for score in scores:
    sum = sum + score
cnt = len(scores)

print(int(sum / cnt))