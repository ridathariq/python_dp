a = int(input())
arr = list(map(int, input().split()))
n = int(input())

result = [b // (2 ** n) for b in arr]

print(*result)