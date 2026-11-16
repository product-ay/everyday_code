n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
print(*nums)
print(*list(reversed(nums)))