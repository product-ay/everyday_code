n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
offset = 100
lines = [0] * (offset + 101)

for i in range(n):
    if dir[i] == 'R':
        for j in range(offset, offset + x[i]):
            lines[j] += 1
    else:
        for k in range(offset, x[i], -1):
            lines[k] += 1
print(max(lines))