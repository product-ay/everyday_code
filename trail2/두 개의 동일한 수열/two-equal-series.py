n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

A.sort()
B.sort()

ans = 'Yes'
for i in A:
    if i in B:
        continue
    else:
        ans = 'No'
print(ans)