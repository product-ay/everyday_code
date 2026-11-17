n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines = [0] * 10

for i in segments:
    a, b = i
    for j in range(a-1, b):
        lines[j] += 1
print(max(lines))