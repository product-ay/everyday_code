n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines = [0] * 101

for a, b in segments:
    for j in range(a, b+1):
        lines[j] += 1
print(max(lines))
