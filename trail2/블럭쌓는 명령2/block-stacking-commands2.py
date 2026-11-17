n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

block = [0] * n

for i in commands:
    A, B = i
    for j in range(A-1, B):
        block[j] += 1
print(max(block))