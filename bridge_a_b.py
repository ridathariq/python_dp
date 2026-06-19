n1 = int(input())
n2 = int(input())


a = []
for _ in range(n1):
    a.append(int(input()))


b = []
for _ in range(n2):
    b.append(int(input()))

combined = list(set(a + b))
sort = combined.sort()

n = len(combined)


if n%2 == 0:
    median = (combined[n//2 - 1] + combined[n // 2] ) / 2
else:
    median = combined[n//2]
print("result is : " + str(median))
