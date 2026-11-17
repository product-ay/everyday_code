n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

block = [0] * (n+1)

for a,b in commands:
    for j in range(a, b+1):
        block[j] += 1
print(max(block))